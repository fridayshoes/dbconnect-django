## DBconnect

Porject to connect SQLite DB to djnago project

pip install Django
pip install black
pip install djangorestframework

##

Set up a models.py that has the table structure for SQLite

## Postman operations

Open Postman app, http://127.0.0.1:8000/api/departments
Select GET, press send, should see the following empty table

'''
[]

```


### Add a record

Open a new Postman tab, http://127.0.0.1:8000/api/departments/add
Select POST, Body, Raw, JSON press send, should see the following empty table

'''
{
  "dept_name": "IT",
  "location": "Mumbai",
  "head_of_department": "Amit"
}
```

Select GET, http://127.0.0.1:8000/api/departments press send, should see the populated table

'''
{
"dept_name": "IT",
"location": "Mumbai",
"head_of_department": "Amit"
}

```


### Delete a record

Select GET, http://127.0.0.1:8000/api/departments press send, should see the populated table

'''
{
"dept_name": "IT",
"location": "Mumbai",
"head_of_department": "Amit"
}

```

Select POST, Body, Raw, JSON press send, should see the following empty table

'''
{
"dept_name": "Finance",
"location": "London",
"head_of_department": "David"
}

```


Select GET, http://127.0.0.1:8000/api/departments press send, should see the populated table

'''
{
"dept_name": "IT",
"location": "Mumbai",
"head_of_department": "Amit"
}
{
  "dept_name": "Finance",
  "location": "London",
  "head_of_department": "David"
}
```

Open new pPostman tab, Select DELETE, http://127.0.0.1:8000/api/departments/1/ press send, should see the populated table

'''
{
"message": "Department deleted successfully"
}

```

Select GET, http://127.0.0.1:8000/api/departments press send, should see the populated table

```

{
"dept_name": "Finance",
"location": "London",
"head_of_department": "David"
}

```

```
