# Write a Python program to demonstrate string slicing. 


# Sample string
text = "Python Programming"
print(f"Original string: {text}")
print(f"Length of string: {len(text)}")

# Basic slicing
print("\nBasic Slicing:")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"First 6 characters: {text[:6]}")
print(f"Characters from 7th position to end: {text[7:]}")
print(f"Characters from index 7 to 12: {text[7:13]}")

# Slicing with step
print("\nSlicing with Step:")
print(f"Every other character: {text[::2]}")
print(f"Every third character: {text[::3]}")

# Negative indexing
print("\nNegative Indexing:")
print(f"Last 11 characters: {text[-11:]}")
print(f"Characters between 2nd and 3rd from the end: {text[-3:-1]}")

# Reverse the string
print("\nReversing:")
print(f"Reversed string: {text[::-1]}")



print("------------------------------------------------------------------------------------------------------------------------------------")
# Write a Python program that manipulates and prints strings using various string methods.





# Sample string
text = "  Python Programming is Fun and Useful  "
print(f"Original string: '{text}'")

# Case conversion
print("\nCase Conversion:")
print(f"Uppercase: '{text.upper()}'")
print(f"Lowercase: '{text.lower()}'")
print(f"Title case: '{text.title()}'")
print(f"Swapped case: '{text.swapcase()}'")

# Trimming whitespace
print("\nTrimming Whitespace:")
print(f"Strip whitespace: '{text.strip()}'")
print(f"Left strip: '{text.lstrip()}'")
print(f"Right strip: '{text.rstrip()}'")

# Finding and replacing
print("\nFinding and Replacing:")
print(f"Find 'Fun': {text.find('Fun')}")
print(f"Replace 'Fun' with 'Exciting': '{text.replace('Fun', 'Exciting')}'")

# Splitting and joining
print("\nSplitting and Joining:")
words = text.split()
print(f"Split into words: {words}")
print(f"Join with hyphens: '{'-'.join(words)}'")

# Checking string properties
print("\nString Properties:")
alpha_string = "Python123"
print(f"Is '{alpha_string}' alphanumeric? {alpha_string.isalnum()}")
print(f"Is '{alpha_string}' alphabetic? {alpha_string.isalpha()}")
print(f"Is 'python' in lowercase? {'python'.islower()}")
print(f"Is 'PYTHON' in uppercase? {'PYTHON'.isupper()}")

# Formatting
print("\nFormatting:")
name = "Alice"
age = 25
print(f"Using format(): '{'{} is {} years old'.format(name, age)}'")
print(f"Using f-string: '{f'{name} is {age} years old'}'")

# Count occurrences
print("\nCounting:")
sample = "Mississippi"
print(f"Count of 'i' in '{sample}': {sample.count('i')}")

