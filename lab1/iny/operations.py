def calculate_expression():
    """Вычисление выражения 1 2 3 4 5 = 25"""
    # (1*2+3)*4+5 = (2+3)*4+5 = 5*4+5 = 20+5 = 25
    result = (1 * 2 + 3) * 4 + 5
    return result

def main():
    result = calculate_expression()
    print(result)

if __name__ == "__main__":
    main()