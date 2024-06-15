#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

print(mult_list([1, 2, 3, 4]))  
print(mult_list([2, 5, 6]))    
