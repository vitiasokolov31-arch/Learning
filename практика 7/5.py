nums = [12, -5, 0, 7, 18, -3, 9, 24, 6, 15]
print("Четные:", list(filter(lambda num: num % 2 == 0, nums)))
print('Положительные:', list(filter(lambda num: num > 0, nums)))
print('Кратные 3 и >5:',list(filter(lambda num: num > 5 and num % 3 == 0, nums)))
    