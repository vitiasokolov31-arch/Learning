s1 = input()
s2 = input()
answ = ''
k = 0
for i in s1:
    if i == s2[k]:
        answ += i
        if len(s2) - 1 > k:
            k += 1
if answ == s2:
    print("True")
else:
    print("False")