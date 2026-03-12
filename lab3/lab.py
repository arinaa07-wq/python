def f(lst: list) -> str:
    if not lst:
        return ""
    result = ""
    for item in lst: #для каждого элемента в lst выполни
        if isinstance(item,list):result += f(item)
        else: result += str(item)
    return result
l0=[]
l1=[1,2,3,4,5]
l2=[1,[2,[],[]],[3,[]],4,[[[[5]]]]]
print(f(l0))
print(f(l1))
print(f(l2))

    