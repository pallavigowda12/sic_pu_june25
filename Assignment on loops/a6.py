#sum of even placed digits in a number
input_number = input("Enter a number: ")
sum_even = 0
for i in range(0, len(input_number), 2):
    sum_even += int(input_number[i])
print("Sum of even placed digits:", sum_even)