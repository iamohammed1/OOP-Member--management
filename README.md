# OOP-Member--management
Membership Management System
This is a simple Python-based membership management system that allows users to add, display, and search for members by their first name, membership ID, or status.

Features
Add Members: Add new members with details like first name, last name, membership ID, and membership status.
Display Members: View the list of all added members with their details.
Search Members: Search for a member by membership ID, first name, or membership status.
Clear Screen: The screen is cleared after certain actions for better readability (compatible with both Windows and Unix-like systems).
How to Run
Clone this repository:
git clone https://github.com/iamohammed1/membership-management.git

Navigate to the project directory:
cd membership-management
Run the program:
python membership_management.py
Code Explanation
The main functionality of the program is split into three sections:

Adding new members
Displaying all members
Searching for a member
The Users class holds the details of each member, while the methods like display_members, create_users, and search_member perform actions related to member management.

Technologies Used
Python: The entire program is written in Python.
OS Module: Used to clear the screen depending on the operating system.
Time Module: Used to add delays for better user experience during actions like adding, displaying, or searching members.
Example Usage
Welcome to membership management
Choose an action:
1. Add new member
2. Display all members
3. Search for a member
4. Exit

