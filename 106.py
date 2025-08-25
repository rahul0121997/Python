import threading
import time

def task1():
    for i in range(3):
        print("Task 1 is running")
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task 2 is running")
        time.sleep(1)

# Creating threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Starting threads
t1.start()
t2.start()

# Waiting for both to finish
t1.join()
t2.join()

print("Both tasks are complete.")
