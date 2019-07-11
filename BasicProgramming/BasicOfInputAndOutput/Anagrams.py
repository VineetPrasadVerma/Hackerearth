n = int(input())
first_string = ""
second_string = ""
for _ in range(n):
    first_string = input()
    second_string = input()
first_list = list(first_string)
second_list = list(second_string)
comparing_list = []
if len(first_list) > len(second_list):
    comparing_list = first_list
elif len(first_list) < len(second_list):
    comparing_list = second_list
else:
    comparing_list = first_list
removed_element_list = []
temp_second_list = second_list.copy()
temp_first_list = first_list.copy()
if comparing_list == first_list:
    for i in range(len(comparing_list)):
        for j in range(len(second_list)):
            if comparing_list[i] == second_list[j]:
                removed_element_list.append(temp_second_list.pop(j))
else:
    for i in range(len(comparing_list)):
        for j in range(len(first_list)):
            if comparing_list[i] == first_list[j]:
                removed_element_list.append(first_list.pop(j))

for i in range(len(removed_element_list)):
    comparing_list.remove(removed_element_list[i])
if comparing_list == first_list:
    print(len(comparing_list) + len(temp_second_list))
else:
    print(len(comparing_list) + len(first_list))
