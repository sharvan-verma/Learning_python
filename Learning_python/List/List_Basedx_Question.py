# 41. List Sum
def list_sum(lst):
    """Calculates the sum of elements in a list."""
    return sum(lst)

# 42. List Product
def list_product(lst):
    """Calculates the product of elements in a list."""
    product = 1
    for num in lst:
        product *= num
    return product

# 43. Find Element
def find_element(lst, element):
    """Finds the index of a given element in a list."""
    try:
        return lst.index(element)
    except ValueError:
        return -1  # Return -1 if element is not found

# 44. List Reversal
def list_reversal(lst):
    """Reverses a list."""
    return lst[::-1]

# 45. List Slicing
def list_slicing(lst, start, end):
    """Extracts a sublist from a given list."""
    return lst[start:end]

# 46. List Comprehension (Even Numbers)
def even_numbers(lst):
    """Creates a list of even numbers from a given list."""
    return [num for num in lst if num % 2 == 0]

# 47. List Comprehension (Squares)
def squares(lst):
    """Creates a list of squares of numbers from a given list."""
    return [num**2 for num in lst]

# 48. Merge Lists
def merge_lists(lst1, lst2):
    """Merges two lists into a single list."""
    return lst1 + lst2

# 49. Intersection of Lists
def intersection(lst1, lst2):
    """Finds the common elements between two lists."""
    return list(set(lst1) & set(lst2))

# 50. Difference of Lists
def difference(lst1, lst2):
    """Finds the elements that are in one list but not the other."""
    return list(set(lst1) - set(lst2))

# 51. Rotate List
def rotate_list(lst, positions):
    """Rotates a list by a given number of positions."""
    positions %= len(lst)  # Handle cases where positions > len(lst)
    return lst[-positions:] + lst[:-positions]

# 52. Find Second Largest
def second_largest(lst):
    """Finds the second largest element in a list."""
    unique_lst = sorted(list(set(lst)), reverse=True)
    if len(unique_lst) >= 2:
        return unique_lst[1]
    else:
        return None

# 53. Remove Specific Element
def remove_element(lst, element):
    """Removes a specific element from a list."""
    if element in lst:
        lst.remove(element)
    return lst

# 54. Insert Element
def insert_element(lst, index, element):
    """Inserts an element at a specific index in a list."""
    lst.insert(index, element)
    return lst

# 55. Count Occurrences
def count_occurrences(lst):
    """Counts the occurrences of each element in a list."""
    counts = {}
    for element in lst:
        counts[element] = counts.get(element, 0) + 1
    return counts

# Example Usages:
my_list = [1, 2, 3, 4, 5, 2, 1]
my_list2 = [3, 5, 6, 7]

print("41. List Sum:", list_sum(my_list))
print("42. List Product:", list_product(my_list))
print("43. Find Element (index of 3):", find_element(my_list, 3))
print("44. List Reversal:", list_reversal(my_list))
print("45. List Slicing (1:4):", list_slicing(my_list, 1, 4))
print("46. Even Numbers:", even_numbers(my_list))
print("47. Squares:", squares(my_list))
print("48. Merge Lists:", merge_lists(my_list, my_list2))
print("49. Intersection:", intersection(my_list, my_list2))
print("50. Difference:", difference(my_list, my_list2))
print("51. Rotate List (2 positions):", rotate_list(my_list, 2))
print("52. Second Largest:", second_largest(my_list))
print("53. Remove Element (2):", remove_element(my_list, 2))
print("54. Insert Element (at index 1, 10):", insert_element(my_list, 1, 10))
print("55. Count Occurrences:", count_occurrences(my_list))