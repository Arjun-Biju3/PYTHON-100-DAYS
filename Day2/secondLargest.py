def findSecondLargest(a):
    largest_number = a[0]
    for i in range(len(a)):
        if(a[i]>largest_number):
            largest_number=a[i]
    a.remove(largest_number)

    second_largest = a[0]
    for j in range(len(a)):
        if(a[j]>second_largest):
            second_largest=a[j]

    return second_largest

a = [12,45,23,6,4,8,55,43,46,86,87,76]
print(findSecondLargest(a))
