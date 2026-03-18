from functools import wraps, lru_cache

def mod(mode='global'):
    """
    Декоратор с опциональным параметром mode.
    mode='global' - уникальность между ВСЕМИ вызовами
    mode='local' - уникальность только ВНУТРИ одного вызова
    Поддерживает рекурсивные функции через lru_cache
    """
    def un_z(func):  # Для глобального режима - один set на все вызовы
        if mode == 'global':
            seen = set()
            
            @wraps(func) # сохраняет имя и документацию оригинальной функции
            @lru_cache(None)  # поддержка рекурсии
            def wrapper(*args, **kwargs): # <- принимает ЛЮБЫЕ аргументы
                
                
                # Получаем результат от функции
                result = func(*args, **kwargs)
                
                # Обрабатываем результат (если это список/кортеж)
                if isinstance(result, (list, tuple)):
                    new_items = []
                    for item in result:
                        if item not in seen:
                            seen.add(item)
                            new_items.append(item)
                    return new_items
                else:
                    # Для одиночных значений
                    if result not in seen:
                        seen.add(result)
                        return result
                    return None
            return wrapper
        
        # Для локального режима - новый set на каждый вызов
        elif mode == 'local':
            @wraps(func)  # сохраняет имя и документацию оригинальной функции
            @lru_cache(None)  # поддержка рекурсии
            def wrapper(*args, **kwargs):
                seen = set()  # новый set для каждого вызова
                result = func(*args, **kwargs)
                
                if isinstance(result, (list, tuple)):
                    new_items = []
                    for item in result:
                        if item not in seen:
                            seen.add(item)
                            new_items.append(item)
                    return new_items
                return result
            return wrapper
    
    # Поддержка вызова без параметра
    if callable(mode):
        return un_z(mode)
    return un_z