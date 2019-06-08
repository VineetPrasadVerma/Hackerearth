input_number = int(input())
elements_of_array = input()
list_elements_of_array = [int(i) for i in elements_of_array.split()]
answer = 1
for elements in list_elements_of_array:
    answer = (answer * elements) % (10**9 + 7)
print(answer)
