import csv
from bs4 import BeautifulSoup
import xmlrpc.client
import requests
import base64

url = "http://localhost:8069"
db = 'ecommerce'
username = 'usmonov_uchqun@mail.ru'
password = 'admin_2003'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# authentication
uid = common.authenticate(db, username, password, {})
print(uid)
print("common", common)

if uid:
    models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

    with open('products_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            print(count)
            response = requests.get(row['image'])
            image_data = response.content
            soup = BeautifulSoup(row['description'], 'html.parser')
            clean_text = soup.get_text()
            category_name = row['Category']
            # Check if the category exists
            category_exist = models.execute_kw(db, uid, password, 'product.category', 'search_count',
                                               [[('name', '=', category_name)]])
            if category_exist:
                # Get category ID if it exists
                category_id = models.execute_kw(db, uid, password, 'product.category', 'search',
                                                [[('name', '=', category_name)]], {'limit': 1})
                product_id = models.execute_kw(db, uid, password, 'product.product', 'create', [{
                    'name': row['title'],
                    'description_sale': clean_text,
                    'image_1920': base64.b64encode(image_data).decode('utf-8'),
                    'categ_id': category_id[0],
                    'list_price': float(row['Price']),
                }])
                print("Product created with ID:", product_id)
            else:
                new_category_id = models.execute_kw(db, uid, password, 'product.category', 'create',
                                                    [{'name': category_name}])
                product_id = models.execute_kw(db, uid, password, 'product.product', 'create', [{
                    'name': row['title'],
                    'description_sale': clean_text,
                    'image_1920': base64.b64encode(image_data).decode('utf-8'),
                    'categ_id': new_category_id,
                    'list_price': float(row['Price']),
                }])
                print("Product created with ID:", product_id)

            if count == 1:
                break
