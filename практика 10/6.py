d = {
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
text = input()
for let in text.upper():
    key = str([k for k, value in d.items() if let in value])
    words = ''.join([value for k, value in d.items() if let in value])
    k = 0
    for i in words:
        k += 1
        if i == let:
            break
    if k:
        print(str(key[2]) * k, end='')