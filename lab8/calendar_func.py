# функции для работы с датами и событиями
from PySide6.QtCore import QDate
from database import save_event_to_db, load_events_from_db

_events = {} # Хранит события
def _date_to_key(date):
    """превращает дату по формату для использования дальше"""
    return date.toString("yyyy-MM-dd") 

def load_events():
    """Загружает события из БД при запуске"""
    global _events
    _events = load_events_from_db()

def add_event(date, event):
    """добавляет события которых нет в список и бд"""
    key = _date_to_key(date)
    if key not in _events:
        _events[key]=[]
    _events[key].append(event) #добавляет события которых нет  в список событий в конец списка
    save_event_to_db(key, event) 
def get_events(date):
    """возвращает список событий для указанной даты"""
    key = _date_to_key(date)
    return _events.get(key, [])  # если ключа нет - вернет пустой список а не ошибку

def has_events(date):
    """проверяет есть ли события на дату"""
    key = _date_to_key(date)
    return key in _events

def remove_event(date):
    """удаляет событие по индексу (0 - первое, -1 - последнее)"""
    key = _date_to_key(date)
    if key in _events and _events[key]:
        print("0-удалить первое, -1-последнее, номер-конкретное")
        print([f"{i}:{e}" for i,e in enumerate(_events[key])]) # показывает события с номерами
        idx = int(input("Твой выбор: ")) # пользователь вводит номер
        removed = _events[key].pop(idx) # удаляем событие под этим номером
        if not _events[key]:
            del _events[key]
        return f"Удалено: {removed}"
    return "Событие не найдено"

def clear_events(date):
    """удаляет все события на указанную дату"""
    key = _date_to_key(date)
    if key in _events:
        count = len(_events[key])
        del _events[key]
        return f"Удалено {count} событий"
    return "Событий не было"

def find_events_by_text(search_text):
    """ищет события, содержащие указанный текст"""
    results = [] # список для результатов поиска
    for key, events in _events.items(): # перебирает все даты в словаре
        for event in events: # перебирает каждое событие в списке этой даты
            if search_text.lower() in event.lower(): # содержится ли искомый текст в событии
                results.append((key, event))
    return results

def format_events(date):
    """возвращает строку со списком событий для отображения"""
    events = get_events(date)
    if not events:
        return " Нет событий"
    
    result = "События:\n"
    for i, event in enumerate(events, 1): #нумерует события, начиная с 1
        result += f"  {i}. {event}\n"
    return result
