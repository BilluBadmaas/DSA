def recur_fibo(n):
   return n if n <= 1 else (recur_fibo(n-1) + recur_fibo(n-2)) #

def recur_fact(n):
   return n if n == 1 else n * recur_fact(n-1) #

num = int(input("Enter an integer for calculation: "))

if num > 0:
    print(f"Factorial of {num}: {recur_fact(num)}")
    print(f"Fibonacci sequence:")
    for i in range(num):
        print(recur_fibo(i), end=" ")
else:
    print("Please enter a positive integer.")
