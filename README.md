## Prerequisites for development
```sh
pip install pipenv
pipenv install
pipenv sync --dev
pipenv shell
```

## Prerequisites for production
```sh
pip install pipenv
pipenv install
pipenv sync
pipenv shell
```

## Running
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
