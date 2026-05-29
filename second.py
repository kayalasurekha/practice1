num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)
difference = num1 - num2
print("The difference of", num1, "and", num2, "is:", difference)

# second example

# Basic string operations in Python

# Define a string
text = "Hello, GitHub!"

# Print the string
print("Original string:", text)

# Length of the string
print("Length:", len(text))

# Access characters
print("First character:", text[0])
print("Last character:", text[-1])

# Slicing
print("Substring (0-5):", text[0:5])

# Concatenation
new_text = text + " Welcome!"
print("Concatenated string:", new_text)

# Uppercase and lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Replace
print("Replace GitHub with Python:", text.replace("GitHub", "Python"))

# Split into words
print("Split:", text.split())

# Check if substring exists
print("Does 'GitHub' exist?", "GitHub" in text)
# updated

# Integer program in Python

# Define integers
a = 10
b = 3

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division (float result)
print("Division:", a / b)

# Floor division (integer result)
print("Floor Division:", a // b)

# Modulus (remainder)
print("Modulus:", a % b)

# Exponentiation (power)
print("Exponentiation:", a ** b)

# Comparison
print("Is a greater than b?", a > b)
print("Is a equal to b?", a == b)