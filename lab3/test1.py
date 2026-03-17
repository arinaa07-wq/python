import pytest
from lab3_12 import f #из файла lab1 импортируем функцию f
def test_f():
    """Один тест на все"""
    assert f([])=="None"
    assert f([1])=="1->None"
    assert f([1,2,3])=="1->2->3->None"

    #Вложенные списки
    assert f([1,[2,3],4])=="1->2->3->4->None"
    assert f([1,[2,[3,4]],5])=="1->2->3->4->5->None"

    #Разные типы 
    assert f([1,"Helloy",True])=="1->Helloy->True->None"

    #Пустые вложения 
    assert f([1,[],2,[],3])=="1->2->3->None"