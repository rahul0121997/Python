def digital_root(n):
    s = str(n)
    total = 0
    for i in s:
        total += int(i)
    if len(str(total)) > 1:
        total = digital_root(str(total))
    return total

print(digital_root(12345))