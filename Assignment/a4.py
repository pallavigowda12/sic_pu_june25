#Code to find the count of prime numbers in a number
input_number=input("Enter a number : ")
prime_numbers=["2","3","5","7"]
count=0
for digit in  input_number:
    if digit in prime_numbers:
        count+=1
print("The count of prime numbers are : ",count)