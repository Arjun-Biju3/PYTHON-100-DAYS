def reverse_text(text):
    return text[::-1]


text = input("Enter text to reverse:")
reversed_text = reverse_text(text)
print("reversed text:",reversed_text)