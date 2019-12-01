list = []
num = int(input("Enter number of elements: "))
for i in range(num):
    numbers = int(input("Enter number: "))
    list.append(numbers)
print("Sum of given elements = ", sum(list))