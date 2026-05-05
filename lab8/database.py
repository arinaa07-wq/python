import psycopg2

def get_connection():
    """Возвращает соединение с БД"""
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="mybase",
        user="postgres",
        password="123"
    )

def save_event_to_db(date_key, event_text):
    """Сохраняет событие в базу данных"""
    try:
        conn = get_connection()
        cursor = conn.cursor()  # cоздает курсор (инструмент для отправки команд в базу данных)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS calendar_events (  
                id SERIAL PRIMARY KEY,
                event_date TEXT NOT NULL,
                event_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            ) 
        """) # Создать таблицу если нет, если есть - не трогай    Авто-нумерация   Поле не может быть пустым
        
        cursor.execute("""
            INSERT INTO calendar_events (event_date, event_text)
            VALUES (%s, %s)
        """, (date_key, event_text)) #Вставить в таблицу calendar_events в колонки event_date и event_text
        
        conn.commit() # подтверждает изменения
        cursor.close()
        conn.close()
        print(f"Сохранено в БД: {date_key} - {event_text}") # сообщение что всё сохранено
        
    except Exception as e:
        print(f" Ошибка сохранения: {e}")

def load_events_from_db(): 
    """Загружает все события из базы данных"""
    events_dict = {}
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT event_date, event_text FROM calendar_events") #Отправляет SQL-запрос  выбора  всех дат и текст событий из таблицы
        rows = cursor.fetchall() # забирает все  результаты из запроса
        
        for date_key, event_text in rows: # перебирает каждую запись
            if date_key not in events_dict: # если даты еще нет в словаре - создает для нее пустой список
                events_dict[date_key] = []
            events_dict[date_key].append(event_text) # добавляет событие в список этой даты
        
        cursor.close()
        conn.close()
        print(f"Загружено из БД: {len(rows)} событий")
        
    except Exception as e:
        print(f" Ошибка загрузки: {e}")
    
    return events_dict
