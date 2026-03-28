import pytest
from lab5 import gen_pi #из файла lab5 импортируем функцию gen_pi
def test1():
    """Проверяет правильность цифр"""
    digits = list(gen_pi(5))# вызываем функцию, получаем генератор, превращаем в список
    assert digits == [3, 1, 4, 1, 5] # проверяем, что список равен ожидаемому
def test2():
    """Проверяет вычисление суммы x/(x**2) для первых n цифр""" 
    n = 3 # количество цифр
    digits = gen_pi(n)  # получаем генератор цифр (3, 1, 4)
    result = sum(map(lambda x: x / (x ** 2), digits))# вычисляем сумму
    expected = 1.5833333333333333 # вычисляем сумму
    assert result == pytest.approx(expected)# сравниваем с учётом погрешности
def test3():
    """Проверяет вычисление суммы для другого количества цифр"""
    n = 5# количество цифр
    digits = gen_pi(n)# получаем генератор цифр (3, 1, 4,1,5)
    result = sum(map(lambda x: x / (x ** 2), digits))# вычисляем сумму
    expected = 2.783333333333333 # вычисляем сумму
    assert result == pytest.approx(expected) # сравниваем с учётом погрешности

