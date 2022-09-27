# The simplest Rippple transactions info service


### Starting up

```git clone git@github.com:Stasyanz/cyprus.git && cd cyprus```

```pip install -r requirements.txt```

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py createsuperuser```

```python manage.py runserver```

Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


### Adding transactions for another address you want to watch

```GET /api/get-data/<ripple address here>```

Sample request: [http://127.0.0.1:8000/api/get-data/rEb8TK3gBgk5auZkwc6sHnwrGVJH8DuaLh/](http://127.0.0.1:8000/api/get-data/rEb8TK3gBgk5auZkwc6sHnwrGVJH8DuaLh/)
