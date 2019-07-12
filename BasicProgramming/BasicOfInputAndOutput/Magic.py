no_of_zeroes = 0
no_of_ones = 0
dict_count_no_of_zeroes_and_ones = {}
for i in range(1, 91):
    if i == 1:
        no_of_zeroes = 1
        dict_count_no_of_zeroes_and_ones[i] = (no_of_zeroes, no_of_ones)
    else:
        temp = no_of_zeroes
        no_of_zeroes += no_of_ones
        no_of_ones = temp
        dict_count_no_of_zeroes_and_ones[i] = (no_of_zeroes, no_of_ones)

for i in range(int(input())):
    t = dict_count_no_of_zeroes_and_ones[int(input())]
    print(t[-1], t[0])
