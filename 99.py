s = "hello world"

s3 = ""
s1 = s.split()

for substring in s1:
    for char in range(len(substring)):
        if char == 0 or char == len(substring) - 1:
            s3 = s3 + substring[char].upper()
        else:
            s3 = s3 + substring[char]
print(s3)        