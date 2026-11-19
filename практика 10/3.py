mx = 0
with open("olimp.txt") as f:
    for line in f:
        for elem in line.split():
            if elem.isdigit():
                if int(elem) > mx:
                    mx2 = mx
                    mx = int(elem)

print(mx2)