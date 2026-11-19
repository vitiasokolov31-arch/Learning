import json
mn = 2027
flag = 'True'
with open("movies.json") as f:
    data = json.load(f)
    print(data['database_name'])
    print(len(data['movies']))
    for movie in data['movies']:
        for key, value in movie.items():
            if key == 'year':
                if int(value) < mn:
                    mn = int(value)
    for movie in data['movies']:
        for key, value in movie.items():
            if value == mn:
                flag = 'False'
        if flag == 'False':
            print(movie["title"], movie["year"])
            break

