#To Print the prime numbers in a decreasing or in instance of m and n
m=int(input())
n=int(input())
prime_numbers=[]
for digit in range(m,n+1):
    if digit>1:
        is_prime=True
        for i in (2,digit+1):
            if(digit%i)==0:
                isPrime=False
        if is_prime:
            prime_numbers.append(digit)

print(prime_numbers)