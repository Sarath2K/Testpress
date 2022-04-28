list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input())
    list.append(element)

minNum = min(list)
maxNum = max(list)
print(list)
print(maxNum, minNum)
