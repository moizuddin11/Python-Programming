def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

list1 = [1, 3, 2, 4, 1, 3, 2, 4, 5, 7, 6, 8, 9, 1, 0, 2]
print(Repeat(list1))