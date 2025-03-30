# 71. Set Operations: Perform union, intersection, and difference operations on sets.
def set_operations(set1, set2):
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set1_2 = set1.difference(set2)
    difference_set2_1 = set2.difference(set1)
    return union_set, intersection_set, difference_set1_2, difference_set2_1

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union, intersection, diff1_2, diff2_1 = set_operations(set1, set2)
print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference (set1 - set2): {diff1_2}")
print(f"Difference (set2 - set1): {diff2_1}")

# 72. Check Subset: Check if one set is a subset of another.
def is_subset(set1, set2):
    return set1.issubset(set2)

set3 = {1, 2}
set4 = {1, 2, 3, 4}
print(f"Is {set3} a subset of {set4}? {is_subset(set3, set4)}")
print(f"Is {set4} a subset of {set3}? {is_subset(set4, set3)}")

# 73. Add and Remove Elements: Add and remove elements from a set.
def add_remove_elements(my_set, add_element, remove_element):
    my_set.add(add_element)
    my_set.discard(remove_element)  # discard does not raise error if element not present
    return my_set

my_set = {1, 2, 3}
my_set = add_remove_elements(my_set, 4, 2)
print(f"Set after adding and removing: {my_set}")

# 74. Map (Square): Use a map function to square each element of a list.
def square_elements(my_list):
    return list(map(lambda x: x**2, my_list))

my_list = [1, 2, 3, 4]
squared_list = square_elements(my_list)
print(f"Squared list: {squared_list}")

# 75. Map (String Length): Use a map function to find the length of each string in a list.
def string_lengths(my_list):
    return list(map(len, my_list))

string_list = ["apple", "banana", "cherry"]
lengths = string_lengths(string_list)
print(f"String lengths: {lengths}")

# 76. Filter (Even Numbers): Use a filter function to get even numbers from a list.
def get_even_numbers(my_list):
    return list(filter(lambda x: x % 2 == 0, my_list))

number_list = [1, 2, 3, 4, 5, 6]
even_numbers = get_even_numbers(number_list)
print(f"Even numbers: {even_numbers}")

# 77. Filter (Prime Numbers): Use a filter function to get prime numbers from a list.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(my_list):
    return list(filter(is_prime, my_list))

prime_list = [2, 3, 4, 5, 6, 7, 8, 9, 11,13]
prime_numbers = get_prime_numbers(prime_list)
print(f"Prime numbers: {prime_numbers}")

# 78. Reduce (Sum): Use a reduce function to find the sum of elements in a list.
from functools import reduce

def sum_elements(my_list):
    return reduce(lambda x, y: x + y, my_list)

sum_list = [1, 2, 3, 4, 5]
sum_result = sum_elements(sum_list)
print(f"Sum of elements: {sum_result}")

# 79. Reduce (Product): Use a reduce function to find the product of elements in a list.
def product_elements(my_list):
    return reduce(lambda x, y: x * y, my_list)

product_list = [1, 2, 3, 4, 5]
product_result = product_elements(product_list)
print(f"Product of elements: {product_result}")

# 80. Set from List: Convert a list to a set and back to a list.
def list_to_set_to_list(my_list):
    my_set = set(my_list)
    return list(my_set)

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list_to_set_to_list(original_list)
print(f"Unique list: {unique_list}")