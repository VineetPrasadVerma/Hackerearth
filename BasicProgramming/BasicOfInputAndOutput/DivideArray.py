size = int(input())
arr = list(map(int, input().split()))
dividing_number_dict = {}
dividing_number_list = []
for i in range(int(input())):
    dividing_number_list.append(int(input()))
for j in dividing_number_list:
    if j in dividing_number_dict:
        dividing_number_dict[j] += 1
    else:
        dividing_number_dict[j] = 1
print(dividing_number_dict)
for key in dividing_number_dict.keys():
    if key != 1:
        if dividing_number_dict[key]*key != 10:
            arr = [j//(dividing_number_dict[key]*key) for j in arr]
        else:
            for i in range(dividing_number_dict[key]):
                arr = [j // key for j in arr]
print(" ".join(str(i) for i in arr))

#     arr = [j//num for j in arr]
# #
# #
# # print(" ".join(str(i) for i in arr))