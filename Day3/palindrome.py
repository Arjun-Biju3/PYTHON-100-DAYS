def check(text):
    if(text == text[::-1]):
        return True
    return False


text = input("Enter text to check:")
palindrome = check(text)
if(palindrome):
    print(text ,"is a palindrome")
else:
    print(text ,"is not a palindrome")