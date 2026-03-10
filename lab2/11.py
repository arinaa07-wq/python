from itertools import*
def f():
    k=0
    alf='НАСТЯ'
    for x in product(alf, repeat=6):
        s="".join(x)
        if s.count('А')<=1 and s.count('Я')<=1:
            k=k+1
    return(k)        
print(f())