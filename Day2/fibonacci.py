def fibonacci(num):
    if num==0:
        print("Enter a valid number")
        return
    if num == 1:
        print("0")
        return
    first_number = 0
    second_number = 1
    print(first_number)
    print(second_number)
    for i in range(2,num):
        third_number = first_number+second_number
        print(third_number)
        first_number=second_number
        second_number=third_number

fibonacci(5)