# creating an empty list
lst = []

# number of elemetns as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst.append(ele)
key = int(input("Enter Key: "))
# print("Checking if 8 exists in list ( using loop ) : ")

for i in lst:
    if (i == key):
        print("Element Exists")
    else:
        print("Element not exist!")