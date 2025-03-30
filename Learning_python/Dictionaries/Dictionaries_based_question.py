# 56. Create Dictionary
def create_dictionary(keys, values):
    """Creates a dictionary with given keys and values."""
    return dict(zip(keys, values))

# 57. Access Value
def access_value(dictionary, key):
    """Accesses a value using a key."""
    return dictionary.get(key)

# 58. Add Key-Value
def add_key_value(dictionary, key, value):
    """Adds a new key-value pair to a dictionary."""
    dictionary[key] = value
    return dictionary

# 59. Update Value
def update_value(dictionary, key, new_value):
    """Updates the value of an existing key."""
    if key in dictionary:
        dictionary[key] = new_value
    return dictionary

# 60. Remove Key
def remove_key(dictionary, key):
    """Removes a key-value pair from a dictionary."""
    if key in dictionary:
        del dictionary[key]
    return dictionary

# 61. Iterate Dictionary
def iterate_dictionary(dictionary):
    """Iterates through a dictionary and prints keys and values."""
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")

# 62. Check Key Existence
def check_key_existence(dictionary, key):
    """Checks if a key exists in a dictionary."""
    return key in dictionary

# 63. Dictionary Comprehension
def dictionary_comprehension(lst):
    """Creates a dictionary using dictionary comprehension."""
    return {x: x**2 for x in lst}

# 64. Merge Dictionaries
def merge_dictionaries(dict1, dict2):
    """Merges two dictionaries."""
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# 65. Sort Dictionary
def sort_dictionary(dictionary, by='key'):
    """Sorts a dictionary by keys or values."""
    if by == 'key':
        return dict(sorted(dictionary.items()))
    elif by == 'value':
        return dict(sorted(dictionary.items(), key=lambda item: item[1]))
    else:
        return dictionary

# 66. Count Character Frequency
def count_char_frequency(string):
    """Counts the frequency of characters in a string using a dictionary."""
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

# 67. Group by Key
def group_by_key(list_of_dicts, key_to_group):
    """Groups a list of dictionaries by a specific key."""
    grouped = {}
    for item in list_of_dicts:
        group_value = item.get(key_to_group)
        if group_value:
            if group_value not in grouped:
                grouped[group_value] = []
            grouped[group_value].append(item)
    return grouped

# 68. Find Max Value
def find_max_value_key(dictionary):
    """Finds the key with the maximum value in a dictionary."""
    return max(dictionary, key=dictionary.get) if dictionary else None

# 69. Reverse Key-Value
def reverse_key_value(dictionary):
    """Reverses the keys and values of a dictionary."""
    return {value: key for key, value in dictionary.items()}

# 70. Word Frequency
def word_frequency(sentence):
    """Counts the frequency of words in a sentence using a dictionary."""
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Example Usages:
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = create_dictionary(keys, values)

print("56. Create Dictionary:", my_dict)
print("57. Access Value (b):", access_value(my_dict, 'b'))
print("58. Add Key-Value:", add_key_value(my_dict, 'd', 4))
print("59. Update Value (c):", update_value(my_dict, 'c', 5))
print("60. Remove Key (a):", remove_key(my_dict, 'a'))
print("61. Iterate Dictionary:")
iterate_dictionary(my_dict)
print("62. Check Key Existence (b):", check_key_existence(my_dict, 'b'))
print("63. Dictionary Comprehension:", dictionary_comprehension([1, 2, 3]))

dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4}
print("64. Merge Dictionaries:", merge_dictionaries(dict1, dict2))
print("65. Sort Dictionary (by key):", sort_dictionary(dict2))
print("65. Sort Dictionary (by value):", sort_dictionary(dict2, 'value'))

print("66. Count Character Frequency:", count_char_frequency("hello world"))

list_of_dicts = [{'name': 'Alice', 'city': 'NY'}, {'name': 'Bob', 'city': 'LA'}, {'name': 'Charlie', 'city': 'NY'}]
print("67. Group by Key (city):", group_by_key(list_of_dicts, 'city'))

print("68. Find Max Value Key:", find_max_value_key({'a': 10, 'b': 5, 'c': 20}))
print("69. Reverse Key-Value:", reverse_key_value({'a': 1, 'b': 2}))
print("70. Word Frequency:", word_frequency("this is a test this is"))