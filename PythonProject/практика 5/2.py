N = int(input())
for i in range(N):
    print((("#" * i) +("#") +  ("#" * i)).rjust(N + i))
print("#". rjust(N))