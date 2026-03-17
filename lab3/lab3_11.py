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

# Добавляем стрелки при печати
for lst in [l0, l1, l2]:
    res = f(lst)
    if res:
        print('->'.join(res) + '->None')
    else:
        print('None')