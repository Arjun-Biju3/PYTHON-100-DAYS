def check_palindorme(text):
    reverse_text_list = []
    reversed_text=""
    for i in text:
        reverse_text_list.append(i)
    for j in reversed(reverse_text_list):
        reversed_text += j
    if text == reversed_text:
        return True
    return False
 
result = check_palindorme("abc")
if result:
    print("Palindrome")
else:
    print("Not palindrome")