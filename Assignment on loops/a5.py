#To Print the prime numbers in a decreasing or in instance of m and n
m=int(input())
n=int(input())
prime_numbers=[]
for digit in range(m,n+1):
    if digit>1:
        is_prime=True
        for i in range(2,int(digit*0.5)+1):
            if(digit%i)==0:
                is_prime=False
        if is_prime:
            prime_numbers.append(digit)
decreasing_order=sorted(prime_numbers, reverse=True)
print(decreasing_order)