import time

seconds = 10
for i in range(seconds, -1, -1):
    print(f"Time left: {i} seconds", end='\r')
    time.sleep(1)
print("Time's up!")