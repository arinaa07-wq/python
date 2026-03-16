def f(a):
    if a==1 or a==0: return 1
    a0=1
    a1=1
    a_n=0
    for n in range(2, a + 1):
        a_n=a0+a0/(2**(n-2))
        a0,a1=a1,a_n
    return a_n if a>1 else 1
print(f(5))
    
