import json

with open("Files/playlist.json") as f:
    playlist_dict = json.load(f)

print("Список всех жанров:")
for genre in playlist_dict:
    print(genre, end=' ')

wish = input("\n\nКакой жанр вы хотите послушать?\n").title()
if wish in playlist_dict:
    print("Подходящая музыка для вас:")
    for song in playlist_dict[wish]:
        print(song)
else:
    print("Такого жанра нет")

new_music = input("Хотите ли вы добавить свою песню?\n").lower()
if new_music in ['да', 'yes', 'y', 'хочу', 'можно', 'д']:
    music_name = input("Название песни: ")
    music_genre = input("Жанр песни: ").title()
    playlist_dict[music_genre] = playlist_dict.get(music_genre, []) + [music_name]

with open("Files/playlist.json", "w") as f:
    json.dump(playlist_dict, f, ensure_ascii=False, indent=4)
    print("Песня успешно добавлена")