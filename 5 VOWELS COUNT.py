# 5.Write a function that counts the number of vowels in a string.



def value(a):
    count = 0  
    for num in a:  
        if num in 'AEIOUaeiou':  
            count += 1  
    return count  
b = input("Enter the word: ")  
print(value(b)) 