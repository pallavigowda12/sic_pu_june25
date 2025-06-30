#code to find largest digit in a number

input_number=input("Enter a number: ")
largest="0"
for digit in input_number:
    if digit>largest:
        largest=digit

print(largest)