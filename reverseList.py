array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(array)
for i in range(n // 2):
    temp = array[i]
    array[i] = array[n - i - 1]
    array[n - i - 1] = temp

print(array)