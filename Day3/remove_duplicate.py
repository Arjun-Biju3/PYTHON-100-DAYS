def remove_duplicate(numbers):
    return list(set(numbers))

numbers = [1,1,7,2,3,2,4,2,1,4,6,4,3,5,7,3,4,6,5,4,3,2]
unique = remove_duplicate(numbers)
print(unique)