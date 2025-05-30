def reverseOfText(text):
    reversed_text=""
    list_text = []
    for i in text:
        list_text.append(i)
    # for j in reversed(list_text):
    #     reversed_text += j
    k=reversed(list_text)
    reversed_text="".join(k)
    return reversed_text


text = "hai"
result = reverseOfText(text)
print(result)
