def traverse(arr):
    # count = 0
    # temp = 1
    # for i in range(0, len(arr)):
    #     if temp % 2 == 0:
    #         count = 2
    #         temp += 1
    #         for j in range(0, len(arr)):
    #             print(arr[i][count], end = " ")
    #             count -= 1
    #     else:
    #         count = 0
    #         temp += 1
    #         for j in range(0, len(arr)):
    #             print(arr[i][count], end = " ")
    #             count += 1
    for i in range(0, len(arr)):
        if i % 2 == 0:
            for j in range(0, len(arr)):
                print(arr[i][j], end = " ")
        else:
            for j in range(len(arr)-1, -1, -1):
                print(arr[i][j], end = " ")


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
traverse(arr)