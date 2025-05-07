'''
Models module for Hotel Management System
This module contains all the business logic classes.
'''
import datetime
from db_connection import DatabaseConnection

class Person:
    """Base class for all people in the system"""
    
    def __init__(self, name, phone, address):
        """Initialize a person with basic information"""
        self.name = name
        self.phone = phone
        self.address = address
        
    def validate_phone(self):
        """Validate phone number format"""
        # Remove any non-digit characters
        digits = ''.join(filter(str.isdigit, self.phone))
        # Check if the length is appropriate (10-15 digits)
        return 10 <= len(digits) <= 15

    def validate_name(self):
        """Validate name"""
        return len(self.name.strip()) > 2  # Name should be at least 3 characters

    def validate_address(self):
        """Validate address"""
        return len(self.address.strip()) > 5  # Address should be at least 6 characters


class Guest(Person):
    """Class to represent a guest in the hotel"""
    
    def __init__(self, name, phone, address, id_proof, room_number, room_type):
        """Initialize a guest with required information"""
        super().__init__(name, phone, address)
        self.id_proof = id_proof
        self.room_number = room_number
        self.room_type = room_type
        
        # Private attribute for balance (encapsulation)
        self.__balance = 0
        
        # Set rates based on room type
        self._set_room_rate()
        
    def _set_room_rate(self):
        """Set room rate based on room type"""
        rates = {
            "Standard": 1000,
            "Deluxe": 2000,
            "Suite": 3500,
            "Executive": 5000
        }
        self.room_rate = rates.get(self.room_type, 1000)  # Default to Standard rate
        
    def validate_id_proof(self):
        """Validate ID proof"""
        return len(self.id_proof.strip()) >= 5
        
    def validate_room_number(self):
        """Validate room number"""
        try:
            room_num = int(self.room_number)
            return 100 <= room_num <= 999  # Room numbers between 100 and 999
        except ValueError:
            return False
            
    def validate_room_type(self):
        """Validate room type"""
        valid_types = ["Standard", "Deluxe", "Suite", "Executive"]
        return self.room_type in valid_types
        
    def validate_all(self):
        """Validate all guest attributes"""
        validations = [
            (self.validate_name(), "Invalid name. Must be at least 3 characters."),
            (self.validate_phone(), "Invalid phone number. Must be 10-15 digits."),
            (self.validate_address(), "Invalid address. Must be at least 6 characters."),
            (self.validate_id_proof(), "Invalid ID proof. Must be at least 5 characters."),
            (self.validate_room_number(), "Invalid room number. Must be between 100 and 999."),
            (self.validate_room_type(), "Invalid room type. Must be Standard, Deluxe, Suite, or Executive.")
        ]
        
        errors = [msg for valid, msg in validations if not valid]
        return (len(errors) == 0, errors)
    
    # Property getter for private balance attribute
    @property
    def balance(self):
        """Get the current balance"""
        return self.__balance
    
    # Property setter for private balance attribute
    @balance.setter
    def balance(self, value):
        """Set the balance value"""
        if isinstance(value, (int, float)) and value >= 0:
            self.__balance = value
        else:
            raise ValueError("Balance must be a non-negative number")
            
    def save_to_db(self, db_connection):
        """Save guest information to database"""
        try:
            query = """
                INSERT INTO guests (
                    name, phone, address, id_proof, check_in_date, 
                    room_number, room_type, room_rate, is_checked_out
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            params = (
                self.name, self.phone, self.address, self.id_proof, 
                datetime.datetime.now(), self.room_number, self.room_type, 
                self.room_rate, False
            )
            
            guest_id = db_connection.execute_update(query, params)
            return guest_id
        except Exception as e:
            print(f"Error saving guest: {e}")
            return None


class HotelManagement:
    """Class to handle hotel management operations"""
    
    def __init__(self):
        """Initialize hotel management system"""
        self.db = DatabaseConnection()
        connection = self.db.connect()
        if not connection:
            raise Exception("Failed to connect to database. Please check your MariaDB configuration.")
        
    def check_in_guest(self, guest):
        """Check in a new guest"""
        # Validate guest details
        is_valid, errors = guest.validate_all()
        if not is_valid:
            return False, errors
            
        # Check if room is available
        room_available = self.is_room_available(guest.room_number)
        if not room_available:
            return False, ["Room is already occupied."]
            
        # Save guest to database
        guest_id = guest.save_to_db(self.db)
        if guest_id:
            return True, ["Guest checked in successfully!"]
        else:
            return False, ["Failed to check in guest. Database error."]
    
    def is_room_available(self, room_number):
        """Check if a room is available"""
        query = """
            SELECT COUNT(*) as count FROM guests 
            WHERE room_number = ? AND is_checked_out = FALSE
        """
        result = self.db.execute_query(query, (room_number,))
        if result and result[0]['count'] == 0:
            return True
        return False
    
    def get_all_guests(self, active_only=True):
        """Get all guests from database"""
        query = """
            SELECT * FROM guests
        """
        if active_only:
            query += " WHERE is_checked_out = FALSE"
            
        result = self.db.execute_query(query)
        return result
    
    def get_guest_by_id(self, guest_id):
        """Get guest by ID"""
        query = "SELECT * FROM guests WHERE guest_id = ?"
        result = self.db.execute_query(query, (guest_id,))
        if result:
            return result[0]
        return None
        
    def get_guest_by_room(self, room_number):
        """Get guest by room number"""
        query = """
            SELECT * FROM guests 
            WHERE room_number = ? AND is_checked_out = FALSE
        """
        result = self.db.execute_query(query, (room_number,))
        if result:
            return result[0]
        return None
    
    def check_out_guest(self, guest_id):
        """Check out a guest"""
        # Get guest details
        guest = self.get_guest_by_id(guest_id)
        if not guest:
            return False, "Guest not found"
            
        # Calculate stay duration and charges
        check_in = guest['check_in_date']
        check_out = datetime.datetime.now()
        
        # Calculate number of days (minimum 1 day)
        delta = check_out - check_in
        days = max(1, delta.days + (1 if delta.seconds > 0 else 0))
        
        # Calculate total charges
        total_amount = days * guest['room_rate']
        
        # Update guest record
        update_query = """
            UPDATE guests SET 
            check_out_date = ?, 
            is_checked_out = TRUE 
            WHERE guest_id = ?
        """
        self.db.execute_update(update_query, (check_out, guest_id))
        
        # Record payment
        payment_query = """
            INSERT INTO payments (
                guest_id, amount, payment_date, payment_method
            ) VALUES (?, ?, ?, ?)
        """
        self.db.execute_update(payment_query, (guest_id, total_amount, check_out, "Cash"))
        
        # Return success and receipt data
        receipt_data = {
            "guest_name": guest['name'],
            "room_number": guest['room_number'],
            "room_type": guest['room_type'],
            "check_in": check_in,
            "check_out": check_out,
            "days": days,
            "rate_per_day": guest['room_rate'],
            "total_amount": total_amount
        }
        
        return True, receipt_data
    
    def close(self):
        """Close database connection"""
        self.db.close()