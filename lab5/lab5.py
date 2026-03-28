#Генератор цифр числа π. Поделите каждую цифру на её квадрат и найдите сумму этих значений
def gen_pi(n):
    """Генератор первых n цифр числа π"""
    pi_digits = "3141592653589793"
    for i in range(n):
        yield int(pi_digits[i])# берёт i-й символ строки, превращает в число

# Используем генератор и map
n = 3
digits = gen_pi(n)
result = sum(map(lambda x: x / (x **2), digits)) #Применяет к каждому из digits
print(result)