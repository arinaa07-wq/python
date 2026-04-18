import psycopg2

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

# ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ВСЕХ ЗАПИСЕЙ 
def get_history():
    """Возвращает все записи из таблицы calculations"""
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
        return rows
    except Exception as e:
        print(f"Ошибка: {e}")
        return []