def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

num=int(input("Enter number whose fact is to be printed : "))
if num<0:
    print("Factorial can not be calculated for negative no")
else:
    print("Factorial of given number = ",factorial(num))
