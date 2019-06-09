n = input()
answer_list = []
for alphabets in n:
    if alphabets.islower():
        answer_list.append(alphabets.upper())
    else:
        answer_list.append(alphabets.lower())
answer_string = ""
print(answer_string.join(answer_list))