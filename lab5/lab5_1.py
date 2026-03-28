pi = "31415926535897932384626433832795"
def pi_digits():
    for d in pi:
        yield int(d)
from functools import reduce
result = reduce(lambda acc, x: acc + (1/x if x != 0 else 0), pi_digits(),0) 
print(result)