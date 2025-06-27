#code to find second smallest digit in a number
input_number=int(input("Enter a number : "))
smallest_number=9
second_smallest=9
while input_number>0:
    digit=input_number%10
    if digit<smallest_number:
        second_smallest=smallest_number
        smallest_number=digit
    elif second_smallest<digit<smallest_number:
        second_smallest=digit
    input_number//=10
print("the second smallest number is : ",second_smallest)
    
