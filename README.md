## odoo-template

# How to run this project?

### Linux
1. Odoo uchun alohida Postgres da user yaratib olamiz.
```bash
sudo su - postgres -c "createuser -s odoo"
```
2. **postgres** useridan foydalanib psqlga kiramiz.
```bash
sudo -u postgres psql
```

3. Yaratilgan userga parol biriktiramiz, **password** o'rniga o'zingiz istagan parolni yozing.
```sql
ALTER ROLE odoo WITH PASSWORD 'password';
```

4. Vertual muhit yaratamiz.
```bash
python3.10 -m venv venv
```

5. Vertual muhitni active holatga keltiramiz.
```bash
source venv/bin/activate
```

6. Kerakli package-larni o'rnatib olamiz.
```bash
sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev
```

7. Odooning o'zida kerak bo'ladigan packagelarni **pip** orqali o'rnatib olamiz.
```bash
python3 -m pip install -r requirements.txt
```

8. Quyidagi buyruqni kiritamiz.
```bash
sudo apt install plocate
```

9. Kelib chiqgan ikki path-ning birinchisini **copy** qilib olamiz
```bash
locate pg_hba.conf
```

10. Olingan```path```ni ichiga kirib **peer** ni **trust** ga o'zgartiramiz.
```bash
sudo nano <.../pg_hba.conf>
```

11. PostgreSQLga restart bermiz.
```bash
sudo /etc/init.d/postgresql restart
```


11. **odoo.conf** faylini sozlaymiz.
```conf
[options]

db_host = False
db_port = False
db_user = odoo
db_password = {userga biriktirgan parolingiz.}
addons_path = addons # custom addons qo'shilsa , bilan ajratib papka nomini berib keting.
default_productivity_apps = True
```

12. Odooni ishga tushirish.
```bash
python3.10 odoo-bin -c debian/odoo.conf -d <database name>
```

### Windows 
1. Odoo uchun alohida Postgres da user yaratib olamiz.
```bash
psql -U postgres -c "CREATE USER odoo WITH SUPERUSER;"
```
2. **postgres** useridan foydalanib psqlga kiramiz.
 - psql deb qidiring va oching,
 - So'ralgan ma'lumotlarni kiriting
 - Password ni kiriting


3. Yaratilgan userga parol biriktiramiz, **password** o'rniga o'zingiz istagan parolni yozing.
```sql
ALTER ROLE odoo WITH PASSWORD 'password';
```

4. Vertual muhit yaratamiz.
```bash
python -m venv venv
```

5. Vertual muhitni active holatga keltiramiz.
```bash
source venv/Scripts/activate
```

6. Kerakli package-larni o'rnatib olamiz.
```bash
sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev
```

7. Odooning o'zida kerak bo'ladigan packagelarni **pip** orqali o'rnatib olamiz.
```bash
pip install -r requirements.txt
```

8. **odoo.conf** faylini sozlaymiz.
```conf
[options]

db_host = False
db_port = False
db_user = odoo
db_password = {userga biriktirgan parolingiz.}
addons_path = addons # custom addons qo'shilsa , bilan ajratib papka nomini berib keting.
default_productivity_apps = True
```

9. Odooni ishga tushirish.
```bash
python odoo-bin -c <odoo.conf file path> -d <database name>
```
### MacOs
1. Odoo uchun alohida Postgres da user yaratib olamiz.
```bash
sudo su - postgres -c "createuser -s odoo"
```
2. **postgres** useridan foydalanib psqlga kiramiz.
```bash
psql postgres
```

3. Yaratilgan userga parol biriktiramiz, **password** o'rniga o'zingiz istagan parolni yozing.
```sql
ALTER ROLE odoo WITH PASSWORD 'password';
```

4. Vertual muhit yaratamiz.
```bash
python3.10 -m venv venv
```

5. Vertual muhitni active holatga keltiramiz.
```bash
source venv/bin/activate
```
6. Kerakli package-larni o'rnatib olamiz.
```bash
brew install openldap
brew install postgresql
brew install libsasl2
```

7. Odooning o'zida kerak bo'ladigan packagelarni **pip** orqali o'rnatib olamiz.
```bash
python3 -m pip install -r requirements.txt
```

8. **odoo.conf** faylini sozlaymiz.
```conf
[options]

db_host = False
db_port = False
db_user = odoo
db_password = {userga biriktirgan parolingiz.}
addons_path = addons # custom addons qo'shilsa , bilan ajratib papka nomini berib keting.
default_productivity_apps = True
```

9. Odooni ishga tushirish.
```bash
python3.10 odoo-bin -c debian/odoo.conf -d <database name>
```
