# Chat-boy aiogram Shop
Магазин для продажи товаров через мессенджер Telegram.

---
## Стек
- Python 3.10
- aiogram
- SQLite
___

## Техническое задание

Разработать чат-бота для продажи товаров через мессенджер телеграмм (хранение данных во внешней ДБ).

---
### Особенности приложения
#### Режим пользователя
- Просмотр каталога товаров внутри телеграм-чата.
- Корзина покупок клиента.
- Возможность заказа товара с указанием места отправки.
- Система просмотра заказов клиента.
- Система отправки вопросов администратору.

#### Режим администратора
- Добавление, удаление, редактирование данных в каталоге товаров.
- Система просмотра всех заказов и их обработки.
- Реализован механизм ответов на вопросы клиентов из ДБ.

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone git@github.com:kireev20000/Chat_boy_aiogram_Shop.git
```
***- Установите зависимости из файла requirements.txt:***
```
pip install -r requirements.txt
```

***- Cоздать и заполнить .env файл в корневой директории:***
```
BOT_TOKEN='токен_бота'
```
## Об авторе <a id=7></a>

Киреев Александр Олегович  
Python-разработчик (Backend)  
E-mail: kireev20000@yandex.ru
Telegram: @kireev20000
