## DBconnect

Porject to connect SQLite DB to djnago project

pip install Django
pip install black
pip install djangorestframework

##

Set up a models.py that has the table structure for SQLite

## Check with postman

Open Postman app, http://127.0.0.1:8000/api/departments
Select GET, press send, should see the following empty table

'''
[]

```


Open a new Postman tab, http://127.0.0.1:8000/api/departments/add
Select POST, Body, Raw, JSON press send, should see the following empty table

'''
{
  "dept_name": "IT",
  "location": "Mumbai",
  "head_of_department": "Amit"
}
```

Select GET, press send, should see the populated table

'''
{
"dept_name": "IT",
"location": "Mumbai",
"head_of_department": "Amit"
}

```

```
