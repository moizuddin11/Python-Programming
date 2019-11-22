def checkKey(dict, key):
    if key in dict.keys():
        print("Present, ", end=" ")
        print("value =", dict[key])
    else:
        print("Not present")

dict = {'a': 0, 'b': 0, 'c': 7}

key = input("Enter key: ")
checkKey(dict, key)