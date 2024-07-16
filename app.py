'''
Данный проект представляет собой простое десктопное приложение,
разработанное с использованием библиотеки Flet для Python,
которое позволяет добавлять новых пользователей в базу данных MongoDB.

Основные функции проекта:
1) Подключение к локальной базе данных MongoDB с использованием библиотеки PyMongo.
2) Создание коллекции "users" в базе данных "mydatabase" для хранения информации о пользователях.
3) Создание формы для ввода данных пользователя, включающей поля для имени, фамилии, отчества и адреса электронной почты.
4) Функция `add_user`, которая обрабатывает нажатие кнопки "Добавить" и добавляет нового пользователя в базу данных MongoDB.
5) Отображение сообщения об успешном добавлении данных или об ошибке при добавлении пользователя с помощью SnackBar.

В целом, проект предоставляет пользователю возможность добавлять новых пользователей в базу данных MongoDB, используя простой и интуитивно понятный интерфейс.
'''

import flet as ft
from pymongo import MongoClient

def main(page: ft.Page):
    page.title = 'Наименование приложения' # Запись данных в MongoDB
    page.window_width = 500 # 480
    page.window_height = 550 # 500
    page.window_resizable = True # False
    page.theme_mode = ft.ThemeMode.LIGHT

    client = MongoClient("mongodb://localhost:27017/") # ⬅️ пишем необходимый локальный адрес
    db = client["mydatabase"] # ⬅️ указываем наименование базы данных
    collection = db["users"] # ⬅️ указываем наименование коллекции базы данных
    
    def add_user(e):
        try:
            name = name_field.value
            surname = surname_field.value
            fathername = fathername_field.value
            email = email_field.value
            collection.insert_one({"name": name,
                                   "surname": surname,
                                   "fathername": fathername,
                                   "email": email})
            page.update()
            page.snack_bar = ft.SnackBar(ft.Text("Данные успешно добавлены"), open=True)
        except Exception as e:
            page.update()
            page.snack_bar = ft.SnackBar(ft.Text(f"Ошибка: {str(e)}"), open=True)
    
    name_field = ft.TextField(label="Введите имя")
    surname_field = ft.TextField(label="Введите фамилию")
    fathername_field = ft.TextField(label="Введите отчество")
    email_field = ft.TextField(label="Введите e-mail")
    add_button = ft.ElevatedButton("Добавить", on_click=add_user)
    
    page.add(
        ft.Text("   Добавление пользователя", size=20, weight=ft.FontWeight.BOLD),
        ft.Container(
            padding=ft.padding.all(16),
            content=ft.Column([
                ft.Row([ft.Text("Имя:        "), name_field]),
                ft.Row([ft.Text("Фамилия:"), surname_field]),
                ft.Row([ft.Text("Отчество:"), fathername_field]),
                ft.Row([ft.Text("E-mail:     "), email_field]),
                ft.Row([]),
                add_button,
            ]),
        ),
    )

ft.app(target=main)

# TODO: Заметки
## Преподаватель: Дуплей Максим Игоревич
## Дата: 16/07/2024