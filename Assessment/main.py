'''
Main module for Hotel Management System
This is the entry point of the application.
'''
import tkinter as tk
from hotel_gui import HotelManagementApp

def main():
    """Main function to run the application"""
    try:
        # Create root window
        root = tk.Tk()
        
        # Create app instance
        app = HotelManagementApp(root)
        
        # Run main loop
        root.mainloop()
        
    except Exception as e:
        print(f"Error starting application: {e}")

if __name__ == "__main__":
    main()