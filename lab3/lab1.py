def f(lst: list) -> str:
    """Преобразует список (включая вложенные)в сторку"""
    if not lst:
        return ""
    result = ""
    for item in lst: #для каждого элемента в lst выполни
        if isinstance(item,list):result += f(item)# если элемент список то рекурсивно вызываем f для него
        else: result += str(item) #если результат число то преобразуем в строку и добавляем
    return result
l0=[]
l1=[1,2,3,4,5]
l2=[1,[2,[],[]],[3,[]],4,[[[[5]]]]]
print(f(l0))
print(f(l1))
print(f(l2))