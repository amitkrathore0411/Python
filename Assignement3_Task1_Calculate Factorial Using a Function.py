def factorial(n):
    fact=1;
    for i in range(n,1,-1):
        fact*=i;
    return fact

num=int(input("Enter number whose fact is to be printed : "))
print(factorial(num))