def window(lst, window_size):
    ans = []
    for i in range(len(lst) - window_size + 1):
        ans.append(tuple(lst[i:i + window_size]))
    return ans
список = [1,2,3,4,5,6,7,8,9,0]
window_size = 3
print(window(список, window_size))