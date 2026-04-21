def analyze_flowers():
    """Анализ цветов в саду и на лугу"""
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
    
    garden_set = set(garden)
    meadow_set = set(meadow)
    
    all_flowers = garden_set | meadow_set
    both_places = garden_set & meadow_set
    only_garden = garden_set - meadow_set
    only_meadow = meadow_set - garden_set
    
    return all_flowers, both_places, only_garden, only_meadow

def main():
    all_flowers, both_places, only_garden, only_meadow = analyze_flowers()
    
    print(all_flowers)
    print(both_places)
    print(only_garden)
    print(only_meadow)

if __name__ == "__main__":
    main()