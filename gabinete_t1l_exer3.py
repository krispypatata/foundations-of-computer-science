# Write a program that takes an integer n and prints the first n prime integers. 

print("\nThis program takes an integer n and prints the first n prime numbers.", end="\n\n")

prime_number=2
counter = 0
n = int(input("Enter n: "))
while counter < n:
    if all(prime_number%i!=0 for i in range(2, prime_number)):
    		print(prime_number)
    		counter = counter + 1

    prime_number = prime_number + 1

