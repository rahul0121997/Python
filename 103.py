s = "abcdeaeiou"
kevin = 0
stuart = 0
for i in range(len(s)):
    if s[i] in "aeiou":
        stuart += len(s) - i
    else:
        kevin += len(s) - i
        
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

print("Player2 (Kevin):", kevin)
print("Player1 (Stuart):", stuart)
