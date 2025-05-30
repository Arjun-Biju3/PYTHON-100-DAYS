def find_missing(numbers):
    last_element = numbers[-1]
    for i in range(1,last_element):
        if numbers[i-1] != i:
            return i
    return "No Missing number found"   
missing = find_missing([1,2,4,5,6,7])
print(missing)