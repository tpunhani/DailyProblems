
# Problem: Given an array of integers, return a new array such that each element 
# at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
def productOfAll(passed_list) -> list:
    prod = 1
    left_products = list()
    for i num in passed_list:         
         prod  *= num
         left_products.append(prod)
    prod = 1
    right_products = list()
    for num in passed_list[::-1]:
         prod *= num
         right_products.append(prod)
    right_products = right_products[::-1]
    result = list() 
    for i in range(len(passed_list)):
         if i==0:
            result.append(left_products[1])
         elif i == len(passed_list)-1:
            result.append(right_products[1])
         else:
            result.append(left_products[i-1] * right_products[i+1])
    return result



