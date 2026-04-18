from abc import ABC, abstractmethod #ABC — делает класс абстрактным. abstractmethod — заставляет дочерние классы реализовать метод
class Vehicle(ABC): #создали класс
    def __init__(self, name, base_speed, base_consumption):
        self._name = name # атрибут: название 
        self._base_speed = base_speed  # атрибут: базовая скорость 
        self._base_consumption = base_consumption # атрибут: базовый расход приватное поле _
#   managed-атрибуты
    @property
    def name(self):
        return self._name
    @property
    def base_speed(self):
        return self._base_speed
    @property
    def base_consumption(self):
        return self._base_consumption
    
    @abstractmethod# пустой абстрактный метод скорости
    def get_speed(self, is_loaded): #self объект, для которого вызывается метод
        pass 
    @abstractmethod# пустой абстрактный метод растояния и цены 
    def get_consumption(self, is_loaded):
        pass 
#   dunder-метод
    def __str__(self): #для пользователя 
        return f"Транспорт: {self._name}"
    def __repr__(self):  #для отладки
        return f"Vehicle('{self._name}', {self._base_speed}, {self._base_consumption})"
    
class PassengerCar(Vehicle): #иерархия наследования ABC - Vehicle - PassengerCar
    def __init__(self, name, base_speed, base_consumption, num_doors=4):
        super().__init__(name, base_speed, base_consumption) # передает данные родителю, чтобы он создал свои атрибуты
        self._num_doors = num_doors
    @property  
    def num_doors(self):  
        return self._num_doors
    
    def get_speed(self, is_loaded):
        if is_loaded == True: return self._base_speed - 15  # скорость меньше на 15
        else: return self._base_speed  # обычная скорость

    def get_consumption(self, is_loaded):
        if is_loaded: return self._base_consumption * 1.5
        return self._base_consumption #вернули базовый расход топлива
    
    def __str__(self): #для пользователя 
        return  f" Легковой: {self._name} | {self._base_speed} км/ч | {self._num_doors} двери"
    def __repr__(self): #для отладки
        return f"PassengerCar('{self._name}', {self._base_speed}, {self._base_consumption}, {self._num_doors})"
    
class Truck(Vehicle):
    def __init__(self, name, base_speed, base_consumption):
        super().__init__(name, base_speed, base_consumption)

    def get_speed(self, is_loaded):
        if is_loaded: return 60  # груженый 60 км/ч
        return 70      # пустой 70 км/ч
    
    def get_consumption(self, is_loaded):
        if is_loaded: return self._base_consumption * 1.8
        return self._base_consumption #вернули базовый расход топлива
    
    def __str__(self): #для пользователя 
        return  f" Грузовой: {self._name} | {self._base_speed} км/ч "
    def __repr__(self): #для отладки
        return f"Truck('{self._name}', {self._base_speed}, {self._base_consumption})"
    
class Bus(Vehicle):
    def __init__(self, name, base_speed, base_consumption):
        super().__init__(name,base_speed, base_consumption)

    def get_speed(self, is_loaded):
        if is_loaded: return 40  # груженый 40 км/ч
        return 50      # пустой 50 км/ч
    
    def get_consumption(self, is_loaded):
        if is_loaded: return self._base_consumption * 1.9
        return self._base_consumption #вернули базовый расход топлива
    
    def __str__(self): #для пользователя 
        return  f" Пассажирский: {self._name} | {self._base_speed} км/ч "
    def __repr__(self): #для отладки
        return f"Bus('{self._name}', {self._base_speed}, {self._base_consumption})"