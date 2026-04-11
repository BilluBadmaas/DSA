# Fibonacci Series
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    
nterms = int(input("Enter a number: "))

# Check if the number of terms is valid 

if nterms<=0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Sequence: ")
    for i in range(nterms):
        print(recur_fibo(i))
        