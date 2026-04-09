"""
Автомобили:
Легковой
Грузовой
Пассажирский
Расчёт расхода топлива в зависимости от загрузки, расчёт стоимости и времени поездки.

"""
from PySide6.QtWidgets import*
from PySide6.QtCore import Qt
import sys 

import psycopg2 #фуекция для работы с бд

app = QApplication(sys.argv)

# ФУНКЦИЯ ДЛЯ СОХРАНЕНИЯ В БД
def save_to_db(distance, car_type, is_loaded, calc_type, result): 
    """
    СОХРАНЯЕТ РЕЗУЛЬТАТ РАСЧЕТА В БАЗУ ДАННЫХ 
    ЧТО ПРИНИМАЕТ:
        distance (float) - расстояние в километрах
        car_type (str)   - тип автомобиля ("Легковой", "Грузовой", "Пассажирский")
        is_loaded (bool) - груженый? (True/False)
        calc_type (str)  - тип расчета ("ВРЕМЯ" или "ТОПЛИВО")
        result (str)     - результат расчета 
    ЧТО ДЕЛАЕТ:
        1. Подключается к PostgreSQL
        2. Создает таблицу если её нет
        3. Вставляет новую строку с переданными данными
        4. Закрывает соединение
        5. Выводит в консоль "Сохранено!" или "Ошибка":
        Ничего не возвращает. Просто сохраняет данные или печатает ошибку.
    """
    try:
       # ПОДКЛЮЧАЕМСЯ К БАЗЕ
       conn = psycopg2.connect( #в переменной conn храниться соединение
            host="localhost",  #База на этом же компьютере
            port=5432, #Порт
            database="mybase", #Имя базы данных
            user="postgres", #Логин для входа
            password="123" #Пароль
        )
       cursor = conn.cursor() #инструмент, через который будем отправлять команды
        # СОЗДАЕМ ТАБЛИЦУ (ЕСЛИ НЕТ)
        #Отправляет SQL-запрос в базу данных СОЗДАТЬ ТАБЛИЦУ, если её ещё нет, с именем "calculations"
        #создаем таблицу  SERIAL PRIMARY KEY номер строчки автоматически 
       cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS calculations (
                id SERIAL PRIMARY KEY,
                distance FLOAT,
                car_type TEXT,
                is_loaded BOOLEAN,
                calc_type TEXT,
                result TEXT
            )
        """) 
        # СОХРАНЯЕМ ДАННЫЕ (ВСТАВЛЯЕМ СТРОКУ В ТАБЛИЦУ)
        # Кладем в таблицу наши значения расстояние, тип авто...
        #cursor.execute- Отправляет команду в бд.
        #INSERT INTO calculations-в какую таблицу вставлять и в какие колонки вставлять данные
        #VALUES (%s, %s, %s, %s, %s)-какие значения вставлять
       cursor.execute(""" 
            INSERT INTO calculations (distance, car_type, is_loaded, calc_type, result)
            VALUES (%s, %s, %s, %s, %s)
        """, (distance, car_type, is_loaded, calc_type, result)) #Кортеж из переменных, которые встанут вместо %s
       conn.commit() #подтверждает изменения в базе данных
       cursor.close()#закрывает инструмент для запросов к базе данных
       conn.close()#Закрывает соединение с базой данных(программа больше не может общаться с БД)
       print("Сохранено в базу данных!")
    except Exception as e:
        print(f"Ошибка: {e}")

# ФУНКЦИЯ ДЛЯ ПОКАЗА ИСТОРИИ
def show_history():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="mybase",
            user="postgres",
            password="123"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM calculations ORDER BY id DESC")  #Запрашивает все данные из таблицы calculations, отсортированные от новых к старым (DESC —от новых к старым)
        rows = cursor.fetchall() #все полученные записи кладем в переменную
        cursor.close()
        conn.close()
         # СОЗДАЕМ ОКНО ДЛЯ ИСТОРИИ
        win = QWidget()
        win.setWindowTitle("История расчетов")
        win.resize(500, 400)
        # СОЗДАЕМ ТЕКСТОВОЕ ПОЛЕ
        text = QTextEdit()
        text.setReadOnly(True)
        # ФОРМИРУЕМ ТЕКСТ
        if rows: # Если есть записи в базе
            result_text = "ВСЕ РАСЧЕТЫ:\n\n"# Пишем заголовок и два переноса строки
            for row in rows: # Перебираем каждую запись по очереди
                result_text = result_text + str(row) + "\n\n" # Добавляем запись к тексту и два переноса
        else: # Если записей нет
            result_text = "Нет расчетов" 
        # ПОКАЗЫВАЕМ ТЕКСТ
        msg = QMessageBox() #Создает пустое диалоговое окно
        msg.setWindowTitle("История расчетов")#Устанавливает заголовок окна
        msg.setText(result_text) #Вставляет текст в окно
        msg.setStandardButtons(QMessageBox.Ok) #Добавляет кнопку "OK" 
        msg.exec() #Показывает окно и ждет
        
    except Exception as e:
        msg = QMessageBox()
        msg.setText(f"Ошибка: {e}")
        msg.exec()


def rast_time():
    """Функция расчета примерного времени поездки"""
    try:
        distance = float(pole.text()) # Получаем расстояние
        #скорость в зависимости от типа авто
        car_type = Spisok.currentText() #Получаем текст из пункта, который сейчас выбран в выпадающем списке 
        if car_type == "Легковой":
            base_speed = 80
        elif car_type == "Грузовой":
            base_speed = 60
        else:  # Пассажирский
            base_speed = 70
        if galochka.isChecked(): # Если груженый - скорость меньше
            base_speed -= 15
    
        time_hours = distance / base_speed # Рассчитываем время в часах
        
        hours = int(time_hours) # отбрасывает дробную часть числа
        minutes = int((time_hours - hours) * 60) #cчитает минуты из дробной части часов
        
        # Выводим результат
        result_label.setText(f" Примерное время: {hours} ч {minutes} мин") #берет метку и пишет в ней новый текст вместо старого
        
        save_to_db(distance, car_type, galochka.isChecked(), "ВРЕМЯ", f"{hours} ч {minutes} мин")

    except ValueError: #если пользователь ввел не число 
        result_label.setText(" Введите корректное расстояние!") #берет метку и пишет в ней новый текст вместо старого

def rast_fuel():
    """Функция расчета расхода и стоимости топлива"""
    try:
        distance = float(pole.text()) # Получаем расстояние
        #расход в зависимости от типа авто
        car_type = Spisok.currentText() #Получаем текст из пункта, который сейчас выбран в выпадающем списке 
        if car_type == "Легковой":
            base_consumption = 8
        elif car_type == "Грузовой":
            base_consumption = 15
        else:  # Пассажирский
            base_consumption = 12
        if galochka.isChecked(): # Если груженый - скорость меньше
            base_consumption *= 1.5
        fuel_liters = (distance / 100) * base_consumption
        total_cost = fuel_liters * 55  # 55 руб за литр
        fuel_label.setText(f"Расход: {fuel_liters:.1f} л | Стоимость: {total_cost:.0f} руб")   
        save_to_db(distance, car_type, galochka.isChecked(), "ТОПЛИВО", f"{fuel_liters:.1f} л {total_cost:.0f} руб") #.1f-Формат: 1 цифра после запятой
    except ValueError:
        fuel_label.setText("Введите корректное расстояние!")

Window = QWidget() #Создает окно
Window.setWindowTitle("Калькулятор расхода топлива") #заголовок окна
Window.resize(400, 300)#размер окна

title = QLabel("Расчёт расхода топлива") #надпись с текстом
title.setStyleSheet("font-size: 16px; font-weight: bold") #стили к метке

group = QGroupBox("Автомобили") # группa с рамкой и заголовком 
Spisok = QComboBox() #cоздает выпадающий список
Spisok.addItems(["Легковой","Грузовой","Пассажирский"]) #добавляет пункты  

galochka = QCheckBox("Груженые") #Создает чекбокс (флажок) с подписью "Груженые"

pole = QLineEdit() #cоздаем поле 
pole.setPlaceholderText("Введите расстояние...")

rast_button= QPushButton("Расчитать время поездки")
rast_button.clicked.connect(rast_time)

fuel_button = QPushButton("Рассчитать расход и стоимость топлива")
fuel_button.clicked.connect(rast_fuel)

history_button = QPushButton("Показать историю расчетов")
history_button.clicked.connect(show_history)

result_label = QLabel("Введите расстояние и нажмите кнопку")
result_label.setStyleSheet("font-size: 14px; color: blue; margin-top: 10px")

fuel_label = QLabel("Введите расстояние и нажмите «Расход»")
fuel_label.setStyleSheet("font-size: 14px; color: green")

group_layout = QVBoxLayout() #Создает вертикальный менеджер компоновки
group_layout.addWidget(Spisok) #Добавляет в выпадающий список 
group_layout.addWidget(galochka)
group_layout.addWidget(pole)
group_layout.addWidget(rast_button)
group_layout.addWidget(fuel_button)
group_layout.addWidget(history_button)

group_layout.addWidget(result_label)
group_layout.addWidget(fuel_label)
group.setLayout(group_layout) #внутри group разложи все вышеперечисленное по правилам  записаным в group_layout

main_layout = QVBoxLayout() #создается вертикальный layout
main_layout.addWidget(title) #сверху добавляем надпись 
main_layout.addWidget(group)# cнизу нашу группу 


Window.setLayout(main_layout)
Window.show()
app.exec()