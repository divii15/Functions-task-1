# 3.Write a function to find the factorial of a given number.




def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
b=int(input("Enter the value:"))
print(fact(b))