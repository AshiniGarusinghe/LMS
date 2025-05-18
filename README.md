## 📚 Library Management System (LMS)
A simple console-based Library Management System built using Python and SQLite. This project allows users to manage book records by adding, searching, issuing, and returning books in a library environment.

## ✅ Features
Add new books
View all books
Search for books by title or author
Issue a book to a user
Return a book
Delete books
Store data persistently using SQLite

## 🛠️ Technologies Used
Python 3
SQLite3 (built-in with Python)
Console-based interface (no GUI yet)

## 📂 Project Structure
library_management_system/
├── main.py         # Main logic and user menu
├── db.py           # Database functions (add, view, search, etc.)
├── library.db      # SQLite database (auto-generated)
└── __pycache__/    # Auto-generated Python cache files

## 🚀 How to Run
Clone the repository (or download manually):
  git clone git clone [https://github.com/AshiniGarusinghe/LMS.git](https://github.com/AshiniGarusinghe/Library-Management-System.git)
  cd library-management-system

Run the program:
  python main.py
  
Follow the on-screen menu to manage books.

## 💾 Database
The system uses SQLite for storing book records. The database file (library.db) will be created automatically the first time you run the program.

## 🔒 Notes
This is a basic version without user login or role management.
  library.db and __pycache__/ should be added to .gitignore.

## 📌 Future Improvements
Add GUI using tkinter
Add user login (admin/librarian)
Export reports to PDF
Generate QR codes for books
Web-based version using Flask or Django


