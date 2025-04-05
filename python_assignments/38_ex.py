# Input string
text = "programming"

# Count characters
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character Counts:", char_count)
