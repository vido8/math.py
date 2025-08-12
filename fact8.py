# factorial

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))
n=int(input(" enter a number: "))
print(n)
result=factorial(n)
print(result)
print(f"factorial of 5 is : {result}")

