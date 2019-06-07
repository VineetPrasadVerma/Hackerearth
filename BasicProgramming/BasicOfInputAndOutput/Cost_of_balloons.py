no_of_test_cases = int(input("Test cases"))

for i in range(0, no_of_test_cases):
    minimum_cost = 0

    cost_of_balloons = input("Cost of balloons")
    cost_of_green_and_purple_balloon = cost_of_balloons.split()
    list_of_costs = []
    for j in cost_of_green_and_purple_balloon:
        list_of_costs.append(int(j))
    max_cost = max(list_of_costs)
    min_cost = min(list_of_costs)

    no_of_participants = int(input("Participants"))
    temp_list = []
    str = ""
    for k in range(0, no_of_participants):
        string_status_of_users = input("Status")
        str += string_status_of_users + " "
        temp_list.append(string_status_of_users)
    status_of_users = str.split()
    count_of_one_on_left = 0
    count_of_one_on_right = 0
    for l in range(0, len(status_of_users), 2):
        if status_of_users[l] == "1":
            count_of_one_on_left += 1
    for m in range(1, len(status_of_users), 2):
        if status_of_users[m] == "1":
            count_of_one_on_right += 1
    left_cost = 0
    right_cost = 0
    if count_of_one_on_left > count_of_one_on_right:
        left_cost = min_cost
        right_cost = max_cost
    else:
        left_cost = max_cost
        right_cost = min_cost

    for n in temp_list:
        stats = n.split()
        if stats[0] == "1" and stats[1] == "1":
            minimum_cost += left_cost + right_cost
        elif stats[0] == "1" and stats[1] == "0":
            minimum_cost += left_cost
        elif stats[0] == "0" and stats[1] == "1":
            minimum_cost += right_cost

    print(minimum_cost)
