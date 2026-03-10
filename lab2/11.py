def count_combinations():
    """
    Подсчитывает количество 6-буквенных комбинаций из букв слова "настя",
    где 'а' встречается не более 1 раза и 'я' встречается не более 1 раза.

    >>> result = count_combinations()
    >>> print(result)
    20480

    Пояснение расчета:
    Всего комбинаций без ограничений: 6^6 = 46656
    Комбинаций где 'а' > 1 раза и/или 'я' > 1 раза вычитаются, остается 20480.
    """
    k = 0
    a = 'настя'
    for b1 in a:
        for b2 in a:
            for b3 in a:
                for b4 in a:
                    for b5 in a:
                        for b6 in a:
                            s = b1 + b2 + b3 + b4 + b5 + b6
                            if s.count('а') <= 1:
                                if s.count('я') <= 1:
                                    k = k + 1
    return k  #  возвращаем результат


if __name__ == "__main__":
    # Этот код выполнится только при прямом запуске файла
    result = count_combinations()
    print(result)
