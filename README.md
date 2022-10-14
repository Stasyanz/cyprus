# The simplest Rippple transactions info service


### Starting up

```git clone git@github.com:Stasyanz/cyprus.git && cd cyprus```

```docker-compose run django python manage.py makemigrations```

```docker-compose run django python manage.py migrate```

```docker-compose run django python manage.py createsuperuser```

```docker-compose up```

Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to add a Wallet address

Sample Wallet address: `rEb8TK3gBgk5auZkwc6sHnwrGVJH8DuaLh`

Transactions are being added on Wallet save

Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for API
