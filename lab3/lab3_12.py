def f(lst: list) -> str:
    rez=""
    stac=[lst]
    while stac: #пока стек не пуст 
        current = stac.pop(0)#берем первый элемент из стека 
        for item in (current):#перебираем все элементы 
             if isinstance(item, list):stac.append(item)#если элемент список то добавляем его в стек 
             else:
                 if rez=="":rez=rez+str(item)#сли число добавляем его к результату
                 else:rez=rez+"->"+ str(item)
    rez=rez+"->None"             
    return rez
l0=[]
l1=[1,2,3,4,5]
l2=[1,[2,[],[]],[3,[]],4,[[[[5]]]]]
print(f(l0))
print(f(l1))
print(f(l2))