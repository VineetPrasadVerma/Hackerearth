n = input()
input_list = [int(i) for i in n.split()]
count = 0
reduced_list = input_list[:-1]
for i in range(reduced_list[0], reduced_list[-1]+1):
    if i % input_list[-1] == 0:
        count += 1
print(count)



























