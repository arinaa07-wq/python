def limit_calls(max_calls): #Объявляем функцию с названием limit_calls, которая принимает один параметр max_calls (максимальное количество вызовов)
    """Декоратор ограничивающий количество вызовов функции"""
    def decorator(func): #объявляем функцию decorator oна принимает параметр func- функция, которую мы декорируем
        """Функция которая изменяет calls"""
        calls=0 # сколько раз вызвали функцию
        def wrapper(*args, **kwargs): # oбъявляем wrapper, принимает  позиционные аргументы *args, именованные аргументы **kwargs.функция будет вызываться ВМЕСТО оригинальной функции.
            nonlocal calls # Разрешаем изменять переменнцю из внешней функции
            if calls >= max_calls: 
                print(f"Функция {func.__name__} достигла лимита вызовов ({max_calls})")
                return None #Оригинальная функция НЕ вызывается.
            calls+=1 #yвеличиваем счетчик вызовов на 1 если лимит еще не достигнут
            print(f"Вызов {calls} из {max_calls}")
            return func (*args, **kwargs)
        return wrapper
    return decorator 
@limit_calls(3)
def say_hello(name):   
    print (f" Привет, {name}!")
say_hello("Aнна")
say_hello("Aнна")
say_hello("Aнна")
say_hello("Aддд")