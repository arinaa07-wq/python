def f(lst):
    rez=""
    stac=[lst]
    while stac:
        current = stac.pop(0)
        for item in (current):
             if isinstance(item, list):stac.append(item)
             else:rez=rez+str(item)
    return rez
l0=[]
l1=[1,2,3,4,5]
l2=[1,[2,[],[]],[3,[]],4,[[[[5]]]]]
print(f(l0))
print(f(l1))
print(f(l2))
