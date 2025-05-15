def sort_list(numbers):
    for i in range( len(numbers)):
        for j in range(len(numbers)-i-1):
            if numbers[j]>numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    return numbers


numbers = [4,3,2,5,1,6]
print(sort_list(numbers))