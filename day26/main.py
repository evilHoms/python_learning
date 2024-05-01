# List comprehension (like arr.map(v => v + 1) in js)
numbers = [1, 2, 3]
inc_numbers = [n + 1 for n in numbers]
print(inc_numbers)

# List comprehension works with all iterrable type (array, strings, range, tupples, ...)
dbl_list = [v * 2 for v in range(1, 5)]
print(dbl_list)

# Conditional list comprehension
even_nums = [v for v in range(1, 5) if v % 2 == 0]
print(even_nums)

# Dictionary comprehension
dict1 = {"one": 1, "two": 2}
dict2 = {v: k for (k, v) in dict1.items()}
print(dict2)