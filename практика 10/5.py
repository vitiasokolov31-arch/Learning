top_words = {}
with open("Files/article.txt") as f:
    for line in f:
        for word in line.lower().split():
            slovo = ''
            for elem in word:
                if elem.isalpha():
                    slovo += elem
            if slovo:
                top_words[slovo] = top_words.get(slovo, 0) + 1
top = sorted(top_words.items(), key=lambda x: x[1], reverse=True)[:5]

for i, (word, count) in enumerate(top, 1):
    print(f"{i}. {word} — {count}")