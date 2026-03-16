def g(a):
    if a==0 or a==1: return 1
    else: return g(a-2)+g(a-1)/(2**(a-1))
for a in range(6):
    print(f"a_{a} = {g(a)}")