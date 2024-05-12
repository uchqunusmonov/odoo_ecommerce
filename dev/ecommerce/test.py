import csv
from bs4 import BeautifulSoup

with open('products_data.csv', 'r') as file:
    reader = csv.reader(file)
    fields = next(reader)
    count = 1
    for row in reader:
        soup = BeautifulSoup(row[1], 'html.parser')
        clean_text = soup.get_text()
        print(count)
        print("Product Name:", row[0])
        print("Description:", clean_text)
        print("Product Image:", row[4])
        print("Product Category:", row[5])
        print("Product Price:", row[7])
        print("Total amount:", row[3])
        count += 1
        if count == 2:
            break
