import pytest
from lab1 import f #из файла lab1 импортируем функцию f
def test_f():
    """Один тест на все"""
    assert f([])==""
    assert f([1])=="1"
    assert f([1,2,3])=="123"

    #Вложенные списки
    assert f([1,[2,3],4])=="1234"
    assert f([1,[2,[3,4]],5])=="12345"

    #Разные типы 
    assert f([1,"Helloy",True])=="1HelloyTrue"

    #Пустые вложения 
    assert f([1,[],2,[],3])=="123"
