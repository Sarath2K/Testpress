list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input())
    list.append(element)

print(list)


def findMaxNum(arr, n):

    arr.sort(reverse=True)
    num = arr[0]
    for i in range(1, n):
        num = num * 10 + arr[i]
    return num


arr = list
n = len(arr)
print(findMaxNum(arr, n))
