from iny import (distance, circle, operations, favoritemovies,
                 myfamily, zoo, songslist, secret, 
                 garden, shopping, store)


def main():
    """Главная функция, объединяющая все задания"""
    print("=" * 50)
    print("ЗАДАНИЕ 1: РАССТОЯНИЯ МЕЖДУ ГОРОДАМИ")
    print("=" * 50)
    distance.main()
    
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 2: ПЛОЩАДЬ КРУГА И ТОЧКИ")
    print("=" * 50)
    circle.main()
    
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 3: МАТЕМАТИЧЕСКОЕ ВЫРАЖЕНИЕ")
    print("=" * 50)
    operations.main()
    
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 4: ФИЛЬМЫ")
    print("=" * 50)
    favoritemovies.main()
    
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 5: МОЯ СЕМЬЯ")
    print("=" * 50)
    myfamily.main()
    
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 6: ЗООПАРК")
    print("=" * 50)
    zoo.main()
    
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 7: ПЕСНИ DEPECHE MODE")
    print("=" * 50)
    songslist.main()
    
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 8: РАСШИФРОВКА СООБЩЕНИЯ")
    print("=" * 50)
    secret.main()
    
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 9: ЦВЕТЫ")
    print("=" * 50)
    garden.main()
    
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 10: МАГАЗИНЫ")
    print("=" * 50)
    shopping.main()
    
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 11: ТОВАРЫ НА СКЛАДЕ")
    print("=" * 50)
    store.main()


if __name__ == "__main__":
    main()