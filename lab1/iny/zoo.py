def manage_zoo():
    """Управление зоопарком"""
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    
    # Посадить медведя между львом и кенгуру
    zoo = zoo[:1] + ['bear'] + zoo[1:]
    
    # Добавить птиц
    birds = ['rooster', 'ostrich', 'lark']
    zoo = zoo + birds
    
    # Убрать слона
    zoo = zoo[:3] + zoo[4:]
    
    # Найти позиции льва и жаворонка
    lion_position = zoo.index('lion') + 1  # +1 для понятного человеку номера
    lark_position = zoo.index('lark') + 1
    
    return zoo, lion_position, lark_position

def main():
    zoo, lion_pos, lark_pos = manage_zoo()
    
    print(zoo)
    print(f"лев сидит в клетке номер {lion_pos}")
    print(f"жаворонок сидит в клетке {lark_pos}")

if __name__ == "__main__":
    main()