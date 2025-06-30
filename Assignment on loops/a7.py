#Sum of odd placed digits in a number
input_number = input("Enter a number: ")
sum_odd = 0
for i in range(0,len(input_number)):
    if (i+1) % 2 != 0:  # Check if the index is odd
        sum_odd += int(input_number[i])
print("Sum of odd placed digits:", sum_odd)