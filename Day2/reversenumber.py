def reverse_number(num):
    if num == 0:
        print("Enter a valid number")
    reversed = 0
    while(num != 0):
        digit = num%10
        reversed = reversed*10 + digit
        num =num // 10 
    return reversed

result = reverse_number(7809)
print("reversed number is:",result)