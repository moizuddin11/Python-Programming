def return_Sum(my_Dict):
    sum = 0
    for i in my_Dict:
        sum = sum + my_Dict[i]
    return sum

dict = {'x': 2, 'y': 4, 'z': 6}
print("Sum :", return_Sum(dict))