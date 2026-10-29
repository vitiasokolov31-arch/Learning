def markdown_to_html(md):
    html = []
    if len(md) == 0:
        return '""'
    for line in md.split("\n"):
        parts = line.split("**")
        line = "".join(f"<b>{p}</b>" if i % 2 else p for i, p in enumerate(parts))
        parts = line.split("`")
        line = "".join(f"<code>{p}</code>" if i%2 else p for i, p in enumerate(parts))
        if line.startswith("#"):
            n = 0
            while n < len(line) and line[n] == "#":
                n += 1
            html.append(f"<h{n}>{line[n+1:]}</h{n}>")
        else:
            html.append(f"<p>{line}</p>")
    return "\n".join(html)


print(markdown_to_html("""# Заголовок
## Подзаголовок
Это **жирный** текст и `код`."""))