num = int(input("Enter a number: "))

def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

divisors = find_divisors(num)

if len(divisors) == 2:
    print(num, "is a prime number.")

else:
    print("Divisors:", divisors)
    print(num, "is not prime")

