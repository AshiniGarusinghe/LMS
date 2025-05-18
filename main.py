import db

def show_menu():
    print("---------- Library Management System ----------")
    print("1. Add New Book")
    print("2. View All Books")
    print("3. Search Books")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

def main():
    db.connect()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Book Title: ")
            author = input("Author: ")
            year = input("Year Published: ")
            db.add_book(title, author, year)
            print("Book added successfully!")

        elif choice == '2':
            books = db.view_books()
            print("\n--- All Books ---")
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Issued To: {book[4]}")

        elif choice == '3':
            keyword = input("Enter title or author to search: ")
            results = db.search_books(keyword)
            if results:
                for book in results:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Issued To: {book[4]}")
            else:
                print("No matching books found.")

        elif choice == '4':
            book_id = input("Enter Book ID to issue: ")
            user = input("Enter user name: ")
            db.issue_book(book_id, user)
            print("Book issued successfully!")

        elif choice == '5':
            book_id = input("Enter Book ID to return: ")
            db.return_book(book_id)
            print("Book returned successfully!")

        elif choice == '6':
            book_id = input("Enter Book ID to delete: ")
            db.delete_book(book_id)
            print("Book deleted successfully!")

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
