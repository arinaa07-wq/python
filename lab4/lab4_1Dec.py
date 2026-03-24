def dec(func):
    def wrapper(*args, **kwargs):
        print("Вызов замыкания ")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper
def un_z(): #Функция для поиска уникальных значений 
    """Замыкание, которое собирает только уникальные значения"""
    seen=set() #Хранит уникальные значения 
    @dec
    def per_z(*args): #Функция перебора значений
        """Принимает любые аргументы и возвращает только новые уникальные"""
        new_items = []
        for item in args:
            if item not in seen:  # если значение новое
                seen.add(item)     # запоминаем его
                new_items.append(item)  # добавляем в результат
        return new_items
    return per_z
rez=un_z()
print(rez(1, 2, 3, 2, 1, 4))
print(rez(5, 1, 2, 6))
print(rez(1, 2, 3, 7,9,0,6,6,4,4,4,4,4))