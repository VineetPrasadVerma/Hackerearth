minimum_dimension = int(input())
no_of_photos = int(input())
list_of_width_and_height = []
for _ in range(no_of_photos):
    width_and_height = input()
    list_of_width_and_height.append(tuple(map(int, (width_and_height.split()))))
for i in list_of_width_and_height:
    if i[0] < minimum_dimension or i[-1] < minimum_dimension:
        print("UPLOAD ANOTHER")
    elif i[0] >= minimum_dimension or i[-1] >= minimum_dimension:
        if i[0] == i[-1]:
            print("ACCEPTED")
        else:
            print("CROP IT")