# Start

###### Обновление пакетов виртуального окружения:
```shell
pip install --upgrade pip
```

###### Установка зависимостей:
```shell
pip install -r requirements.txt
```

###### Создание миграции для БД:
```shell
python manage.py makemigrations
```

###### Миграция данных для таблиц:
```shell
python manage.py migrate
```

###### Загрузить данные в БД:
```shell
python manage.py loaddata data.json
```

###### Создать суперпользователя:
```shell
python manage.py createsuperuser
```

###### Запуск локального сервера:
```shell
python manage.py runserver
```