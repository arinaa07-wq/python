def get_family_info():
    """Информация о семье"""
    my_family = ['мать', 'отец', 'брат']
    
    my_family_height = [
        ['мать', 160],
        ['отец', 190],
        ['брат', 110]
    ]
    
    father_height = my_family_height[1][1]
    total_height = sum(member[1] for member in my_family_height)
    
    return father_height, total_height

def main():
    father_height, total_height = get_family_info()
    
    print(f'рост отца- {father_height} cм')
    print(f'общий рост- {total_height} cм')

if __name__ == "__main__":
    main()