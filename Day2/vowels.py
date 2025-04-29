def count_vowels(text):
    count = 0
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for letter in text:
        if letter in vowels:
            count += 1
    return count

count = count_vowels("arjun")
print("No of vowels:",count)