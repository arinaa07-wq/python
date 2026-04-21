def calculate_distances():
    """Функция для расчета расстояний между городами"""
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }
    
    distances = {}
    for city1 in sites:
        distances[city1] = {}
        for city2 in sites:
            if city1 != city2:
                x1, y1 = sites[city1]
                x2, y2 = sites[city2]
                dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                distances[city1][city2] = dist
    
    return distances

def main():
    distances = calculate_distances()
    print(distances)

if __name__ == "__main__":
    main()