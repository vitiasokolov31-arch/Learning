def tokenize(text):
    result, buf = [], []
    for i, ch in enumerate(text):
        is_sep = ch in ' \t\n.,;:!?()[]{}"«»—='
        is_mid = 0 < i < len(text) - 1 and text[i - 1].isalnum() and text[i + 1].isalnum()

        if is_sep and not (ch == '.' and is_mid) and not (ch in "-'" and is_mid):
            if buf:
                result.append(''.join(buf))
                buf = []
        else:
            buf.append(ch)

    if buf:
        result.append(''.join(buf))
    return result
print(tokenize("Привет, мир! Как дела?"))
print(tokenize("Жили-были 3.14 раза"))
print(tokenize("s = \"don't\""))
print(tokenize("A...B"))
print(tokenize(""))