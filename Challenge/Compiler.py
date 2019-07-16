lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

for line in text.splitlines():
    ind = line.find("//")
    temp = line.find("->")
    if temp <= ind:
        a = line.replace("->", ".")
        print(a)

