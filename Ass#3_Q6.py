<<<<<<< HEAD
def checkKey(dict, key):
    if key in dict.keys():
        print("Present, ", end=" ")
        print("value =", dict[key])
    else:
        print("Not present")

dict = {'a': 0, 'b': 0, 'c': 7}

key = input("Enter key: ")
=======
def checkKey(dict, key):
    if key in dict.keys():
        print("Present, ", end=" ")
        print("value =", dict[key])
    else:
        print("Not present")

dict = {'a': 0, 'b': 0, 'c': 7}

key = input("Enter key: ")
>>>>>>> d23b1ee4bc1c4be2818b2cd47243977c444e04f6
checkKey(dict, key)