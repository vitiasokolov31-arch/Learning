import json

with open("Files/movies.json") as f:
    data = json.load(f)
print(data['database_name'])
print(len(data['movies']))
first = data['movies'][0]
print(first['title'], first['year'])
movies = data['movies']
movies_sorted = sorted(movies, key=lambda m: m['rating'], reverse=True)
for i, movie in enumerate(movies_sorted[:5], 1):
    print(f"{i}. {movie['title']} ({movie['year']}) — Рейтинг: {movie['rating']}")