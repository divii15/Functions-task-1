# 2.Write a function that checks if a number is even or odd.



def val(num):                   
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num1=int(input("Enter the value1: "))
print(val(num1))
num2=int(input("Enter the value2: "))
print(val(num2))
