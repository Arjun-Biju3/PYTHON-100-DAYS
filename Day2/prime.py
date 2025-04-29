def check_prime(number):
    if number <= 1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

result = check_prime(19)
if result:
    print("Number is prime")
else:
    print("Number is not prime")