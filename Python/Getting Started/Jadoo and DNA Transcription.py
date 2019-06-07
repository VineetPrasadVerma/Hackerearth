dna = input()
list = []
str = ""
for i in dna:
    if i == 'G':
        list.append('C')
    elif i == 'C':
        list.append('G')
    elif i == 'T':
        list.append('A')
    elif i == 'A':
        list.append('U')
    else:
        list = "Invalid Input"
        break
print(str.join(list))