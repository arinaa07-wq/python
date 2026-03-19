def limit_calls(max_calls=None):  # 1. ИЗМЕНЕНИЕ: параметр стал опциональным принимает параметр max_calls (по умолчанию None)
    """Декоратор ограничивающий количество вызовов функции
    Если max_calls=None - лимит бесконечный
    Поддерживает рекурсивные функции
    """
    def decorator(func): #объявляем функцию decorator oна принимает параметр func- функция, которую мы декорируем
        calls = 0  # Счетчик внешних вызовов
        in_recursion = False  # 2.ИЗМЕНЕНИЕ: отслеживания рекурсии (находимся внутри рекурсивного вызова или нет)
        def wrapper(*args, **kwargs):
            nonlocal calls, in_recursion # добавляем in_recursion в nonlocal
            if max_calls is None:return func(*args, **kwargs) #3.ИЗМЕНЕНИЕ: если лимит не задан - просто вызываем функцию
            if in_recursion: # 4.ИЗМЕНЕНИЕ: проверяем, не рекурсивный ли это вызов
                return func(*args, **kwargs)#5.ИЗМЕНЕНИЕ: если да - просто вызываем функцию без проверки лимита
            if calls >= max_calls:
                print(f"Функция {func.__name__} достигла лимита вызовов ({max_calls})")
                return None
            calls += 1
            print(f"Вызов {calls} из {max_calls}")
            in_recursion = True  # включаем режим "мы внутри рекурсии"
            result = func(*args, **kwargs)  # вызываем функцию
            in_recursion = False  # выключаем режим
            return result
        return wrapper
    return decorator

#ТЕСТЫ
# ТЕСТ 1: Обычная функция с лимитом 
print("=== Тест 1: Обычная функция ===")
@limit_calls(3)
def say_hello(name):
    print(f" Привет, {name}!")

say_hello("Анна")
say_hello("Анна")
say_hello("Анна")
say_hello("Аддд")  # 4-й вызов - лимит

# ТЕСТ 2: Функция без лимита 
print("\n=== Тест 2: Без лимита ===")
@limit_calls()  # можно вызвать сколько угодно раз
def unlimited_greet(name):
    print(f" Привет, {name}!")

unlimited_greet("Анна")
unlimited_greet("Анна")
unlimited_greet("Анна")
unlimited_greet("Анна")  # 4-й вызов - работает!

# ТЕСТ 3: Рекурсивная функция (НОВАЯ ФИЧА)
print("\n=== Тест 3: Рекурсивная функция ===")
@limit_calls(2)
def factorial(n):
    print(f"  вычисляем factorial({n})")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(f"factorial(5) = {factorial(5)}")  # внутри 5 рекурсивных вызовов, но считается как 1
print(f"factorial(3) = {factorial(3)}")  # Второй внешний вызов - разрешен
print(f"factorial(4) = {factorial(4)}")  # не выполнится