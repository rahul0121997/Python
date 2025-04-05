# Open the file for reading
with open("example.txt", "r") as file:
    # Read some data
    data = file.read(10)  # Read first 10 characters
    print(f"Data read: {data}")
    
    # Check current position of the cursor
    position = file.tell()
    print(f"Current cursor position: {position}")
