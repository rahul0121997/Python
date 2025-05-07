'''
Hotel Management System GUI
This module contains the GUI implementation for the Hotel Management System.
'''
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import datetime
from models import Guest, HotelManagement

class HotelManagementApp:
    """Main GUI application class for Hotel Management System"""
    
    def __init__(self, root):
        """Initialize the GUI application"""
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Initialize hotel management system
        self.hotel = HotelManagement()
        
        # Create notebook for tabbed interface
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create frames for each tab
        self.check_in_frame = ttk.Frame(self.notebook)
        self.guest_list_frame = ttk.Frame(self.notebook)
        self.check_out_frame = ttk.Frame(self.notebook)
        
        # Add frames to notebook
        self.notebook.add(self.check_in_frame, text="Check In")
        self.notebook.add(self.guest_list_frame, text="Guest List")
        self.notebook.add(self.check_out_frame, text="Check Out")
        
        # Set up each frame
        self.setup_check_in_frame()
        self.setup_guest_list_frame()
        self.setup_check_out_frame()
        
        # Protocol for closing the window
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def setup_check_in_frame(self):
        """Set up the check-in frame"""
        # Create frame for form
        form_frame = ttk.LabelFrame(self.check_in_frame, text="Guest Information")
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create input fields
        # Name
        ttk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.name_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.name_var, width=30).grid(row=0, column=1, padx=10, pady=10)
        
        # Phone
        ttk.Label(form_frame, text="Phone:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.phone_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.phone_var, width=30).grid(row=1, column=1, padx=10, pady=10)
        
        # Address
        ttk.Label(form_frame, text="Address:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.address_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.address_var, width=30).grid(row=2, column=1, padx=10, pady=10)
        
        # ID Proof
        ttk.Label(form_frame, text="ID Proof:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.id_proof_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.id_proof_var, width=30).grid(row=3, column=1, padx=10, pady=10)
        
        # Room Number
        ttk.Label(form_frame, text="Room Number:").grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)
        self.room_number_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.room_number_var, width=30).grid(row=0, column=3, padx=10, pady=10)
        
        # Room Type
        ttk.Label(form_frame, text="Room Type:").grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)
        self.room_type_var = tk.StringVar()
        room_types = ["Standard", "Deluxe", "Suite", "Executive"]
        ttk.Combobox(form_frame, textvariable=self.room_type_var, values=room_types, width=27).grid(row=1, column=3, padx=10, pady=10)
        self.room_type_var.set("Standard")  # Default value
        
        # Button frame
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=4, column=0, columnspan=4, pady=20)
        
        # Check In button
        ttk.Button(button_frame, text="Check In", command=self.check_in_guest).pack(side=tk.LEFT, padx=10)
        
        # Clear button
        ttk.Button(button_frame, text="Clear", command=self.clear_check_in_form).pack(side=tk.LEFT, padx=10)
        
    def setup_guest_list_frame(self):
        """Set up the guest list frame"""
        # Create frame for controls
        controls_frame = ttk.Frame(self.guest_list_frame)
        controls_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Refresh button
        ttk.Button(controls_frame, text="Refresh List", command=self.refresh_guest_list).pack(side=tk.LEFT, padx=10)
        
        # Treeview for guest list
        columns = ("guest_id", "name", "phone", "room_number", "room_type", "check_in_date")
        self.guest_tree = ttk.Treeview(self.guest_list_frame, columns=columns, show="headings")
        
        # Configure columns
        self.guest_tree.heading("guest_id", text="ID")
        self.guest_tree.heading("name", text="Name")
        self.guest_tree.heading("phone", text="Phone")
        self.guest_tree.heading("room_number", text="Room")
        self.guest_tree.heading("room_type", text="Type")
        self.guest_tree.heading("check_in_date", text="Check In Date")
        
        # Set column widths
        self.guest_tree.column("guest_id", width=50)
        self.guest_tree.column("name", width=150)
        self.guest_tree.column("phone", width=100)
        self.guest_tree.column("room_number", width=80)
        self.guest_tree.column("room_type", width=100)
        self.guest_tree.column("check_in_date", width=150)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.guest_list_frame, orient=tk.VERTICAL, command=self.guest_tree.yview)
        self.guest_tree.configure(yscroll=scrollbar.set)
        
        # Pack treeview and scrollbar
        self.guest_tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Populate guest list
        self.refresh_guest_list()
        
    def setup_check_out_frame(self):
        """Set up the check-out frame"""
        # Create frame for room input
        input_frame = ttk.LabelFrame(self.check_out_frame, text="Check Out Guest")
        input_frame.pack(fill=tk.X, padx=20, pady=20)
        
        # Room Number
        ttk.Label(input_frame, text="Room Number:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.checkout_room_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.checkout_room_var, width=10).grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        
        # Find Guest button
        ttk.Button(input_frame, text="Find Guest", command=self.find_guest_for_checkout).grid(row=0, column=2, padx=10, pady=10)
        
        # Guest info frame
        self.guest_info_frame = ttk.LabelFrame(self.check_out_frame, text="Guest Information")
        self.guest_info_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Guest info text
        self.guest_info_text = scrolledtext.ScrolledText(self.guest_info_frame, height=10, width=50)
        self.guest_info_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.guest_info_text.config(state=tk.DISABLED)
        
        # Check Out button (initially disabled)
        self.checkout_button = ttk.Button(self.check_out_frame, text="Check Out", command=self.check_out_guest, state=tk.DISABLED)
        self.checkout_button.pack(pady=10)
        
        # Receipt frame
        self.receipt_frame = ttk.LabelFrame(self.check_out_frame, text="Receipt")
        self.receipt_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Receipt text
        self.receipt_text = scrolledtext.ScrolledText(self.receipt_frame, height=10, width=50)
        self.receipt_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.receipt_text.config(state=tk.DISABLED)
        
        # Print button (initially disabled)
        self.print_button = ttk.Button(self.check_out_frame, text="Print Receipt", command=self.print_receipt, state=tk.DISABLED)
        self.print_button.pack(pady=10)
        
    def check_in_guest(self):
        """Handle check-in button click"""
        try:
            # Get values from form
            name = self.name_var.get()
            phone = self.phone_var.get()
            address = self.address_var.get()
            id_proof = self.id_proof_var.get()
            room_number = self.room_number_var.get()
            room_type = self.room_type_var.get()
            
            # Create guest object
            guest = Guest(name, phone, address, id_proof, room_number, room_type)
            
            # Check in guest
            success, message = self.hotel.check_in_guest(guest)
            
            if success:
                messagebox.showinfo("Success", message[0])
                self.clear_check_in_form()
                self.refresh_guest_list()
            else:
                messagebox.showerror("Error", "\n".join(message))
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def clear_check_in_form(self):
        """Clear the check-in form"""
        self.name_var.set("")
        self.phone_var.set("")
        self.address_var.set("")
        self.id_proof_var.set("")
        self.room_number_var.set("")
        self.room_type_var.set("Standard")
        
    def refresh_guest_list(self):
        """Refresh the guest list"""
        # Clear current items
        for item in self.guest_tree.get_children():
            self.guest_tree.delete(item)
            
        # Get guests from database
        guests = self.hotel.get_all_guests()
        
        # Add guests to treeview
        for guest in guests:
            # Format check-in date
            check_in_date = guest['check_in_date'].strftime("%Y-%m-%d %H:%M")
            
            # Add guest to treeview
            self.guest_tree.insert("", tk.END, values=(
                guest['guest_id'],
                guest['name'],
                guest['phone'],
                guest['room_number'],
                guest['room_type'],
                check_in_date
            ))
            
    def find_guest_for_checkout(self):
        """Find guest for checkout"""
        try:
            # Get room number
            room_number = self.checkout_room_var.get()
            
            # Validate room number
            if not room_number:
                messagebox.showerror("Error", "Please enter a room number")
                return
                
            # Find guest
            guest = self.hotel.get_guest_by_room(room_number)
            
            if guest:
                # Store guest ID for checkout
                self.current_checkout_guest_id = guest['guest_id']
                
                # Display guest info
                self.display_guest_info(guest)
                
                # Enable checkout button
                self.checkout_button.config(state=tk.NORMAL)
            else:
                messagebox.showerror("Error", "No guest found in room " + room_number)
                self.clear_checkout_form()
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def display_guest_info(self, guest):
        """Display guest information"""
        # Enable text widget for editing
        self.guest_info_text.config(state=tk.NORMAL)
        
        # Clear current content
        self.guest_info_text.delete(1.0, tk.END)
        
        # Format check-in date
        check_in_date = guest['check_in_date'].strftime("%Y-%m-%d %H:%M")
        
        # Add guest info
        info = f"""Guest ID: {guest['guest_id']}
Name: {guest['name']}
Phone: {guest['phone']}
Address: {guest['address']}
ID Proof: {guest['id_proof']}
Room Number: {guest['room_number']}
Room Type: {guest['room_type']}
Room Rate: ₹{guest['room_rate']} per day
Check-in Date: {check_in_date}
"""
        self.guest_info_text.insert(tk.END, info)
        
        # Disable text widget
        self.guest_info_text.config(state=tk.DISABLED)
        
    def check_out_guest(self):
        """Handle check-out button click"""
        try:
            # Confirm checkout
            confirm = messagebox.askyesno("Confirm Checkout", "Are you sure you want to check out this guest?")
            
            if not confirm:
                return
                
            # Check out guest
            success, receipt_data = self.hotel.check_out_guest(self.current_checkout_guest_id)
            
            if success:
                messagebox.showinfo("Success", "Guest checked out successfully!")
                
                # Display receipt
                self.display_receipt(receipt_data)
                
                # Enable print button
                self.print_button.config(state=tk.NORMAL)
                
                # Disable checkout button
                self.checkout_button.config(state=tk.DISABLED)
                
                # Refresh guest list
                self.refresh_guest_list()
            else:
                messagebox.showerror("Error", receipt_data)
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def display_receipt(self, receipt_data):
        """Display receipt"""
        # Enable text widget for editing
        self.receipt_text.config(state=tk.NORMAL)
        
        # Clear current content
        self.receipt_text.delete(1.0, tk.END)
        
        # Format dates
        check_in_date = receipt_data['check_in'].strftime("%Y-%m-%d %H:%M")
        check_out_date = receipt_data['check_out'].strftime("%Y-%m-%d %H:%M")
        
        # Add receipt info
        receipt = f"""
                          HOTEL MANAGEMENT SYSTEM
                              PAYMENT RECEIPT
                              
=================================================================
Guest Name: {receipt_data['guest_name']}
Room Number: {receipt_data['room_number']}
Room Type: {receipt_data['room_type']}
=================================================================
Check-in Date: {check_in_date}
Check-out Date: {check_out_date}
Duration of Stay: {receipt_data['days']} day(s)
=================================================================
Room Rate: ₹{receipt_data['rate_per_day']:.2f} per day
Total Amount: ₹{receipt_data['total_amount']:.2f}
=================================================================

                        Thank you for your stay!
                           Please visit again!
"""
        self.receipt_text.insert(tk.END, receipt)
        
        # Disable text widget
        self.receipt_text.config(state=tk.DISABLED)
        
    def print_receipt(self):
        """Handle print receipt button click"""
        messagebox.showinfo("Print", "Receipt sent to printer!")
        self.clear_checkout_form()
        
    def clear_checkout_form(self):
        """Clear the checkout form"""
        self.checkout_room_var.set("")
        self.guest_info_text.config(state=tk.NORMAL)
        self.guest_info_text.delete(1.0, tk.END)
        self.guest_info_text.config(state=tk.DISABLED)
        self.receipt_text.config(state=tk.NORMAL)
        self.receipt_text.delete(1.0, tk.END)
        self.receipt_text.config(state=tk.DISABLED)
        self.checkout_button.config(state=tk.DISABLED)
        self.print_button.config(state=tk.DISABLED)
        
    def on_close(self):
        """Handle window close event"""
        try:
            # Close database connection
            self.hotel.close()
            
            # Destroy root window
            self.root.destroy()
        except Exception as e:
            print(f"Error closing application: {e}")
            self.root.destroy()