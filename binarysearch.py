def BinarySearch(list, key):
    low = 0
    high  = len(list1)-1
    Found = False
    while low <= high and not Found:
        mid = (low+high)//2
        if key == list1[mid]:
            Found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if Found == True:
        print("Key Found")
    else:
        print("Key is not Found")

#To get value from Users
num = int(input("Enter the list lenght:"))
list1 = [int(input()) for i in range(num)]

# for default value
#list1 = [28,1,14,12,39]

list1.sort()
print(list1)
key = int(input("Enter the key: "))
BinarySearch(list1, key)
