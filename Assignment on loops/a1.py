#Fibonacci number
first_number=1
second_number=2
n=int(input("enter a number "))
print(first_number)
print(second_number)
for i in range(2,n):
    next_number=first_number+second_number
    print(next_number)
    first_number=second_number
    second_number=next_number
      