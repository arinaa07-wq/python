"""
Автомобили:
Легковой
Грузовой
Пассажирский
Расчёт расхода топлива в зависимости от загрузки, расчёт стоимости и времени поездки.

"""
from PySide6.QtWidgets import*
import sys 

from mypackage.database import save_to_db, get_history
from mypackage.report import save_to_excel

app = QApplication(sys.argv)

def show_history():
    rows = get_history()
    if rows:
        text = "ВСЕ РАСЧЕТЫ:\n\n"
        for r in rows:
            text += f"ID: {r[0]} | {r[1]} км | {r[2]} | Груз: {'Да' if r[3] else 'Нет'} | {r[4]} | {r[5]}\n\n"
    else:
        text = "Нет расчетов"
    msg = QMessageBox()
    msg.setText(text)
    msg.exec()

def save_report():
    rows = get_history()
    if rows:
        save_to_excel(rows, "report.xlsx")
        msg = QMessageBox()
        msg.setText("Сохранено в report.xlsx")
        msg.exec()
    else:
        msg = QMessageBox()
        msg.setText("Нет данных")
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

report_button = QPushButton("Сохранить в Excel")
report_button.clicked.connect(save_report)

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
group_layout.addWidget(report_button)
group_layout.addWidget(result_label)
group_layout.addWidget(fuel_label)
group.setLayout(group_layout) #внутри group разложи все вышеперечисленное по правилам  записаным в group_layout

main_layout = QVBoxLayout() #создается вертикальный layout
main_layout.addWidget(title) #сверху добавляем надпись 
main_layout.addWidget(group)# cнизу нашу группу 


Window.setLayout(main_layout)
Window.show()
app.exec()