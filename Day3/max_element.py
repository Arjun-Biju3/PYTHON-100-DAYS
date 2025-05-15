numbers = [1,1,7,2,3,2,4,2,1,4,100,6,4,3,5,7,3,4,6,5,4,3,2]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i

print(max)