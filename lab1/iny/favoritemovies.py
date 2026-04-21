def extract_movies(movies_string):
    """Извлечение фильмов из строки с помощью срезов"""
    # my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    
    first = movies_string[:10]           # 'Терминатор'
    last = movies_string[-15:]           # 'Назад в будущее'
    second = movies_string[12:25]        # 'Пятый элемент'
    second_from_end = movies_string[-22:-17]  # 'Чужие'
    
    return first, second, second_from_end, last

def main():
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    
    first, second, second_from_end, last = extract_movies(my_favorite_movies)
    
    print(first)
    print(last)
    print(second)
    print(second_from_end)

if __name__ == "__main__":
    main()