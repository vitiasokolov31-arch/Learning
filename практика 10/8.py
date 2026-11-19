import json

with open("playlist.json") as f:
    print("Список всех жанров:")
    playlist_dict = json.load(f)
    for genre in playlist_dict:
        print(genre, end=' ')
    wish = input("\n\nКакой жанр вы хотите послушать?\n").title()
    print(f"Подходящая музыка для вас: {playlist_dict[wish]}")
    new_music = input("Хотите ли вы добавить свою песню?\n").lower()
    if new_music in ['да', 'yes', 'y', 'хочу', 'можно', 'д']:
        music_name = input("Название песни: ")
        music_genre = input("Жанр песни: ").title()
        playlist_dict[music_genre] = playlist_dict.get(music_genre, []) + [music_name]
with open("playlist.json", "w") as f:
    json.dump(playlist_dict, f, ensure_ascii=False, indent=4)
