# Лабороторная работа №7

## Задание 
Перепишите свой вариант ЛР №6 с использованием классов и объектов. Задание то же, вариант GUI фреймворка возьмите следующий по списку. Для успешной сдачи в коде должны присутствовать:

использование абстрактного базового класса и соотвествующих декораторов для методов,
иерархия наследования,
managed - атрибуты,
минимум 2 dunder-метода у каждого класса.

## Визуальный вид окна 
<img width="480" height="524" alt="image" src="https://github.com/user-attachments/assets/e8b31525-4ec9-4f7e-a56b-4a2276be535e" />

## Пример работы 

<img width="483" height="530" alt="image" src="https://github.com/user-attachments/assets/c3b2ab12-e7f7-42ad-b7c6-a678c8796ccf" />
<img width="486" height="335" alt="image" src="https://github.com/user-attachments/assets/bed193aa-a9e1-4619-b1d7-3b8cff9de719" />
<img width="296" height="175" alt="image" src="https://github.com/user-attachments/assets/342c4a57-b379-4f53-b331-ded4093037b1" />

## Ход работы
1. Создала абстрактный класс Vehicle с managed-атрибутами (@property) и абстрактными методами get_speed(), get_consumption()
2. Добавила в Vehicle dunder-методы __str__ и __repr__
3. Создала дочерние классы:
PassengerCar - легковой автомобиль
Truck - грузовой автомобиль
Bus - пассажирский автомобиль

4. Реализовала методы get_speed() и get_consumption() для каждого класса с учетом загрузки

5. Добавила в каждый дочерний класс dunder-методы __str__ и __repr__

6. Создала пакет mypackage с модулями:
vehicles.py - классы автомобилей
database.py - работа с PostgreSQL
report.py - сохранение в Excel
7. Написала GUI на Tkinter:
Создала окно, виджеты (Label, Combobox, Checkbutton, Entry, Button)
Написала функции calculate_time(), calculate_fuel(), show_history(), save_report()
Привязала функции к кнопкам
8. Подключила пакет mypackage к основной программ

## Список использованных источников:
1. [Начало работы с удаленными контейнерами Docker в WSL 2](https://matplotlib.org/cheatsheets/(https://dbader.org/blog/python-first-class-functions))

