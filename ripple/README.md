# The simplest Rippple transactions info service


### Starting up

```git clone <>```

```cd <>>&& cd ripple```

```pip install -r requirements.txt```

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py createsuperuser```

```python manage.py runserver```

Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


### Adding transactions for another address you want to watch

```GET /api/get_data/<ripple address here>```
