n = int(input())
list_of_prime_numbers = []
for number in range(n):
    if number <= 1:
        continue
    else:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            list_of_prime_numbers.append(str(number))

string_numbers = " "
print(string_numbers.join(list_of_prime_numbers))