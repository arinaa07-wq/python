def calculate_circle_area(radius, pi=3.1415926):
    """Расчет площади круга"""
    return round(pi * (radius ** 2), 4)

def is_point_in_circle(point, radius):
    """Проверка, находится ли точка внутри круга"""
    distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
    return distance <= radius

def main():
    rad = 42
    point_1 = (23, 34)
    point_2 = (30, 30)
    
    area = calculate_circle_area(rad)
    print(area)
    print(is_point_in_circle(point_1, rad))
    print(is_point_in_circle(point_2, rad))

if __name__ == "__main__":
    main()