# Hotel Management System

A Python-based GUI application for hotel management using Tkinter and MySQL.

## Project Overview

This hotel management system allows hotel staff to:
- Check-in new guests
- Display a list of all current guests
- Check-out guests
- Generate and print receipts

## Features

- **GUI Application**: Built with Tkinter for an intuitive interface
- **Database Integration**: MySQL for data storage and retrieval
- **Object-Oriented Design**: Follows OOP principles including inheritance and encapsulation
- **Modular Architecture**: Separates database connection, business logic, and UI components
- **Validation**: Comprehensive input validation for all fields
- **Error Handling**: Exception handling to prevent application crashes

## Project Structure

- `db_connection.py`: Database connection and operations
- `models.py`: Business logic and data models
- `hotel_gui.py`: Tkinter GUI implementation
- `main.py`: Application entry point

## Requirements

- Python 3.6+
- MySQL Server
- Required Python packages:
  - tkinter
  - mysql-connector-python

## Setup Instructions

1. **Install required packages**:
   ```
   pip install mysql-connector-python
   ```

2. **Configure MySQL**:
   - Install MySQL Server if not already installed
   - Create a MySQL user or use the root account
   - Update the database connection parameters in `db_connection.py`

3. **Run the application**:
   ```
   python main.py
   ```

## Implementation Details

### Object-Oriented Design

The application implements OOP concepts:
- **Inheritance**: The `Guest` class inherits from the `Person` base class
- **Encapsulation**: Private attributes with getter/setter methods (e.g., `__balance`)
- **Modular Design**: Separation of concerns across multiple classes and files

### Database Design

The system uses two main tables:
- `guests`: Stores all guest information and room assignments
- `payments`: Records payment transactions linked to guests

### Error Handling

The application implements comprehensive error handling:
- Validation of all user inputs
- Exception handling for database operations
- User-friendly error messages

## Usage Guide

### Check In
1. Navigate to the "Check In" tab
2. Fill in all required guest information
3. Click "Check In" button

### View Guests
1. Navigate to the "Guest List" tab
2. View all current guests
3. Click "Refresh List" to update

### Check Out
1. Navigate to the "Check Out" tab
2. Enter the room number
3. Click "Find Guest"
4. Review guest information
5. Click "Check Out" to process checkout
6. View receipt and print if needed

## Future Enhancements

Potential future improvements:
- User authentication system
- Reports and analytics
- Room service management
- Extended booking capabilities
- Customer relationship management features