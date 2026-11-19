top_words = {}
with open("article.txt") as f:
    for line in f:
        for word in line.split():
            slovo = ''
            for elem in word:
                if elem.isalpha():
                    slovo += elem
            top_words[slovo] = top_words.get(slovo, 0) + 1
top_word = sorted([value for value in top_words.values()], reverse=True)[:5]
print(top_words)
for i, k in enumerate(top_word, 1):
    print(f"Топ {i} слово по количеству появлений это -", end=' ')
    print(*[key for key, value in top_words.items() if value == k])