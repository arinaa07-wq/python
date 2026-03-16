import pytest
from math import isclose
from lab3_21 import g #из файла lab1 импортируем функцию f
def test_g():
    """Один тест на все"""
    #Базовые случаи 
    assert g(0)==1
    assert g(1)==1

    #Первые значения 
    assert isclose(g(2),1.5)
    assert isclose(g(3),1.375)
    assert isclose(g(4),1.671875)
    assert isclose(g(5),1.4794921875)


    #Проверка формулы для любого а
    for a in range(2,6):
        assert isclose (g(a),g(a-2)+g(a-1)/(2**(a-1)))