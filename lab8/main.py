import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,  QVBoxLayout, QCalendarWidget, QLabel, QPushButton, QLineEdit
from exceptions import DateSelectionError
from calendar_func import add_event, get_events, has_events, format_events,clear_events, remove_event, find_events_by_text
from calendar_func import load_events
class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("интерактивный календарь")
        self.setGeometry(100,100,600,500)
        central_widget = QWidget() #Создает пустой контейнер
        self.setCentralWidget(central_widget) #главный контейнер для всего 
        layot = QVBoxLayout(central_widget)
        self.calendar = QCalendarWidget()
        self.calendar.selectionChanged.connect(self.on_date_selected)
        self.info_label = QLabel("Выберите дату в календаре")

        self.event_input = QLineEdit()
        self.event_input.setPlaceholderText("Введите событие...")
        self.add_btn = QPushButton("Добавить событие")
        self.add_btn.clicked.connect(self.add_event)
        self.clear_btn = QPushButton(" Очистить все события")
        self.clear_btn.clicked.connect(self.clear_events)
        self.remove_btn = QPushButton(" Удалить одно событие")
        self.remove_btn.clicked.connect(self.remove_one_event)
        self.search_btn = QPushButton(" Найти события")
        self.search_btn.clicked.connect(self.search_events)
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск событий...")
        
        layot.addWidget(self.info_label)
        layot.addWidget(self.calendar)
        layot.addWidget(self.event_input)
        layot.addWidget(self.add_btn)
        layot.addWidget(self.clear_btn)
        layot.addWidget(self.search_input)
        layot.addWidget(self.search_btn)
        layot.addWidget(self.remove_btn)
        load_events()
    def on_date_selected(self):
            """функция вызывающаяся каждый раз когда пользователь выбирает новую дату """
            date = self.calendar.selectedDate() #получает и сохраняет выбранную дату
            if not date.isValid(): # проверяет корекность даты
                self.info_label.setText(" НЕВЕРНАЯ ДАТА") # показывает в текстовой метке
                return
            date_str = date.toString("dd.MM.yyyy") # дату в красивую строку 
            events_text = format_events(date)
            self.info_label.setText(f" {date_str}\n\n{events_text}") # oбновляет текстовую метку на экране

    def add_event(self):
        date = self.calendar.selectedDate()  #получает и сохраняет выбранную дату
        text = self.event_input.text().strip() # берет текст из поля ввода удаляя пробелы
        if not text: #если текста нет 
            self.info_label.setText(" Введите текст")
            return
        add_event(date, text)  # функция из calendar_func
        self.event_input.clear() # очищаем поле 
        self.on_date_selected() # показ списка с новыми событиями 
        self.info_label.setText(f" Добавлено!\n\n{format_events(date)}")
    
    def clear_events(self):
        date = self.calendar.selectedDate() #получает и сохраняет выбранную дату
        if not has_events(date): # если нет событий
            self.info_label.setText(" Нет событий")
            return
        clear_events(date)  # функция из calendar_func
        self.on_date_selected() # показ списка с новыми событиями 
    
    def remove_one_event(self):
        date = self.calendar.selectedDate() #получает и сохраняет выбранную дату
        if not has_events(date):  # если нет событий
            self.info_label.setText(" Нет событий")
            return 
        result = remove_event(date) # возвращает строку с результатом удаления
        self.info_label.setText(f" {result}") # показывает результат удаления в метке
        self.on_date_selected() # показ списка с новыми событиями 
    
    def search_events(self): 
        text = self.search_input.text().strip() # берет текст из поля ввода удаляя пробелы
        if not text: #если текста нет 
            self.info_label.setText("Введите текст")
            return
        results = find_events_by_text(text) # ищет события с указанным текстом
        if not results:  # если не найдено  
            self.info_label.setText(f"Ничего не найдено")
            return
        msg = f" Найдено {len(results)}:\n" # количество найденых событий 
        for key, ev in results: # перебирает все и добавляет дату и событие в сообщение
            msg += f"{key}: {ev}\n"
        self.info_label.setText(msg) #оказ результата на экране
        self.search_input.clear() # очищает поле поиска

if __name__ == "__main__": #запущен ли файл напрямую а не импортирован как модуль
    app = QApplication(sys.argv) # cоздает приложение
    window = CalendarApp() # создается окно с календарем
    window.show()
    sys.exit(app.exec()) #Запускает главный цикл приложения, завершает программу при выходе
