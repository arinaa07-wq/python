def calculate_song_times():
    """Расчет времени звучания песен"""
    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]
    
    # Три песни: 'Halo', 'Enjoy the Silence' и 'Clean'
    time1 = round(violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[8][1], 2)
    
    # Другие три песни: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
    time2 = round(violator_songs_list[1][1] + violator_songs_list[6][1] + violator_songs_list[7][1], 2)
    
    return time1, time2

def main():
    time1, time2 = calculate_song_times()
    print(f'Три песни звучат {time1} минут')
    print(f'А другие три песни звучат {time2} минут')

if __name__ == "__main__":
    main()