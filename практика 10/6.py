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

def to_keypad(text):
    result = ''
    for let in text.upper():
        for key, value in d.items():
            if let in value:
                result += key * (value.index(let) + 1)
                break
    return result

text = input()
print(to_keypad(text))