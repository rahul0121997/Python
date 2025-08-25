s = "abaabab"

half = len(s) // 2
first_half = s[half+1:]
second_half = s[:half]
print(first_half)
print(second_half)

if first_half == second_half:
    print("Symmentric")
else:
    print("not symmentric")
