list = []
num = int(input("Enter number of elements: "))
for i in range(num):
    numbers = int(input("Enter elements: "))
    list.append(numbers)
print("Maximum Number = ", max(list))