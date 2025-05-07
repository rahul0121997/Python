'''
Database connection module for Hotel Management System
This module handles all database operations and connections using MariaDB.
'''
import mariadb
import sys

class DatabaseConnection:
    """Class to handle database connections and operations"""
    
    def __init__(self):
        """Initialize database connection parameters"""
        self.host = "localhost"
        self.user = "root"
        self.password = ""  # Change this to your MariaDB password
        self.database = "hotel_management"
        self.connection = None
        
    def connect(self):
        """Establish connection to MariaDB database"""
        try:
            # Try to connect to MariaDB server
            connection = mariadb.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            
            # Create cursor
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            
            # Close current connection
            cursor.close()
            connection.close()
            
            # Connect to the specific database
            self.connection = mariadb.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            
            # Create tables if they don't exist
            self._create_tables()
            
            return self.connection
            
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            return None
            
    def _create_tables(self):
        """Create necessary tables if they don't exist"""
        try:
            cursor = self.connection.cursor()
            
            # Create guests table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS guests (
                    guest_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    phone VARCHAR(20) NOT NULL,
                    address VARCHAR(255) NOT NULL,
                    id_proof VARCHAR(50) NOT NULL,
                    check_in_date DATETIME NOT NULL,
                    check_out_date DATETIME,
                    room_number INT NOT NULL,
                    room_type VARCHAR(50) NOT NULL,
                    room_rate DECIMAL(10, 2) NOT NULL,
                    is_checked_out BOOLEAN DEFAULT FALSE
                )
            """)
            
            # Create payments table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS payments (
                    payment_id INT AUTO_INCREMENT PRIMARY KEY,
                    guest_id INT NOT NULL,
                    amount DECIMAL(10, 2) NOT NULL,
                    payment_date DATETIME NOT NULL,
                    payment_method VARCHAR(50) NOT NULL,
                    FOREIGN KEY (guest_id) REFERENCES guests(guest_id)
                )
            """)
            
            # Commit changes
            self.connection.commit()
            cursor.close()
            
        except mariadb.Error as e:
            print(f"Error creating tables: {e}")
            
    def execute_query(self, query, params=None):
        """Execute a query and return the result"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
                
            result = cursor.fetchall()
            self.connection.commit()
            cursor.close()
            return result
        except mariadb.Error as e:
            print(f"Error executing query: {e}")
            return None
    
    def execute_update(self, query, params=None):
        """Execute an update query (INSERT, UPDATE, DELETE)"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
                
            self.connection.commit()
            last_id = cursor.lastrowid
            cursor.close()
            return last_id
        except mariadb.Error as e:
            print(f"Error executing update: {e}")
            return None
    
    def close(self):
        """Close the database connection"""
        if self.connection:
            self.connection.close()