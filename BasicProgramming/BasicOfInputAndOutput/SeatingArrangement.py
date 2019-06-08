n = int(input())
for _ in range(n):
    flag = 0
    seat_number = int(input())
    list_of_seat_type = ['WS', 'MS', 'AS', 'AS', 'MS', 'WS']
    seat_type = ""
    for i in range(6, 114, 6):
        difference = 11
        if flag == 0:
            temp = 0
            for j in range(i-6+1, i+1):
                seat_type = list_of_seat_type[temp]
                temp += 1
                flag = 1
                if seat_number in range(i-6+1, i+1):
                    facing_seat_number = j + difference
                    difference -= 2
                    if seat_number == j:
                        print(facing_seat_number, end=" ")
                        print(seat_type)
                        break
        else:
            difference = 1
            temp = 0
            for j in range(i-6+1, i+1):
                seat_type = list_of_seat_type[temp]
                temp += 1
                flag = 0
                if seat_number in range(i-6+1, i+1):
                    facing_seat_number = j - difference
                    difference += 2
                    if seat_number == j:
                        print(facing_seat_number, end=" ")
                        print(seat_type)
                        break