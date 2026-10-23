grades = [" 5 ", "неявка", "4", " хор ", "", "100", "2", "два"]
s = []
s1 = ["отл", "хор", 'уд', 'неуд']
s2 = [5,4,3,2]
for i in grades:
    i = i.rstrip()
    i = i.lstrip()
    if i.isdigit() and 2 <= int(i) <= 5:
        s.append(int(i))
    if i in s1:
        s.append(int(s2[s1.index(i)]))
print(sorted(set(s),reverse=True))