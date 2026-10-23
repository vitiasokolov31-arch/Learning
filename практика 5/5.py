import random
secret = int(random.randint(1,100))
while True:
    numb = int(input())
    if numb > secret:
        print("Меньше")
        continue
    elif numb < secret:
        print("Больше ")
        continue
    else:
        print("Угадал")
        exit()