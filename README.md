# The simplest Rippple transactions info service


### Starting up

```git clone git@github.com:Stasyanz/cyprus.git && cd cyprus```

```pip install -r requirements.txt```

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py createsuperuser```

```python manage.py runserver```

Run Redis in a new terminal window:

```docker-compose up redis```

Run Celery in a new terminal window:

```celery -A balance worker -l INFO```

Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Adding transactions for another address you want to watch

Transactions are being added on Wallet save (in admin interface)
