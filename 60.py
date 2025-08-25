x = ["hello", "world", "hi", "hello world",'hello']

count = 0

for i in x:
    if "hello" in i:
        count += 1
    else:
        pass
    
    
print(count)