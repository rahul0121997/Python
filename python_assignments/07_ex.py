#Practical Example 8: Write a Python program to check if a person is eligible to donate blood
# using a nested if.
def check_blood_donation_eligibility():
    # Get user inputs
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight in kg: "))
    
    # Initialize health status
    health_status = input("Do you have any health issues? (yes/no): ").lower()
    last_donation = input("Have you donated blood in the last 3 months? (yes/no): ").lower()
    
    # Check eligibility using nested if statements
    if age >= 18 and age <= 65:
        if weight >= 50:
            if health_status == "no":
                if last_donation == "no":
                    print("Congratulations! You are eligible to donate blood.")
                else:
                    print("Sorry, you are not eligible. You must wait at least 3 months between donations.")
            else:
                print("Sorry, you are not eligible due to health issues.")
        else:
            print("Sorry, you are not eligible. Minimum weight requirement is 50 kg.")
    else:
        print("Sorry, you are not eligible. Donor age must be between 18 and 65.")

# Run the program
check_blood_donation_eligibility()