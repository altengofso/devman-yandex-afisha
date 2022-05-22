# Куда пойти
Учебный проект на Django.
Сайт о самых интересных местах в Москве.

![image](https://user-images.githubusercontent.com/79760865/169692082-94a796f7-5626-40fb-afd6-a9f6e70a0514.png)

[Демо сайта](http://wheretogoalt.pythonanywhere.com/)

## Как запустить

1. Скачать код
```bash
$ git clone http://github.com/...
```
2. Создать виртуальное окружение, активировать его и установить зависимости из requirements.txt
```bash
$ python3 -m venv /path/to/venv/
$ source /path/to/venv/bin/activate
$ pip3 install -r requirements.txt
```
3. Создать и импортировать миграции
```bash
$ cd /path/to/where-to-go
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
4. Создать суперпользователя
```bash
$ python3 manage.py createsuperuser
```
5. Создать файл с переменными окружения
```bash
$ echo "DEBUG=True" > .env
$ echo "SECRET_KEY=super_secret_key" >> .env
```
6. Запустить сервер
```bash
$ python3 manage.py runserver
```

## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![image](https://user-images.githubusercontent.com/79760865/169692971-e3c60271-23c2-4701-b858-f76e9204b970.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки удалите ключи из Local Storage с помощью Chrome Dev Tools —> Вкладка Application —> Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.

## Наполнение данными

Наполнить базу данных сайта данными можно как через интерфейс администратора http://<адрес сайта>/admin в разделе Places

![image](https://user-images.githubusercontent.com/79760865/169693028-a49717e2-3c3c-4161-a337-8fdada1d9cce.png)

Так и через интерфейс командной строки

```bash
$ python3 manage.py load_place /path/to/json-file
```

JSON файл с подробными данными о локации должен иметь следующий формат:

```javascript
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

Например

```bash
$ python3 manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json
```

Также есть возможность загрузить сразу несколько файлов с информацией о нескольких локациях.
Для этого разместите файлы в одной директории и используйте команду:

```bash
$ python3 manage.py load_places /path/to/places-directory
```

Команда считает все JSON файлы из директории, соответствующие формату и загрузит данные на сайт.

## Загрузка подготовленных тестовых данных

Для загрузки уже подготовленных тестовых данных используйте следующую команду:

```bash
$ python3 manage.py load_places "../where-to-go-places"
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке.

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
