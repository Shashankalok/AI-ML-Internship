# 1_variables.py
a = 10
b = 9.7
name = "Shashank"

print(a, b, name)

# 2_datatypes.py
x = 10
y = "Shashank"
print(type(x))
print(type(y))

# 3_even_odd.py
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4_largest.py
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("A is greater")
else:
    print("B is greater")

    # 5_for_loop.py
for i in range(1, 6):
    print(i)

# 6_while_loop.py
i = 1
while i <= 5:
    print(i)
    i += 1

# 7_sum.py
total = 0
for i in range(1, 6):
    total += i
print("Sum:", total)

# 8_function.py
def add(a, b):
    return a + b
print(add(3, 4))

# 9_factorial.py
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(factorial(5))

# 10_list.py
numbers = [1, 2, 3]
numbers.append(4)
numbers.remove(2)
print(numbers)

# 11_list_sum.py
numbers = [1, 2, 3, 4]
print(sum(numbers))

# 12_dictionary.py
student = {"name": "Shashank", "age": 22}
print(student["name"])

# 13_dict_loop.py
student = {"name": "Shashank", "age": 22}

for key, value in student.items():
    print(key, ":", value)

# 14_count_even.py
numbers = [1, 2, 3, 4, 5, 6]
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Even count:", count)

# 15_reverse.py
text = "Python"
print(text[::-1])

