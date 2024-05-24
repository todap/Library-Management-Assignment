from check import LibraryManagementSystem

def main():
    """
    The main function that runs the Library Management System.
    """
    library = LibraryManagementSystem("books.json", "users.json", "checkouts.json")

    while True:
        choice = main_menu()

        if choice == '1':
            library.add_book_flow()
        elif choice == '2':
            library.list_books()
        elif choice == '3':
            library.search_book_flow()
        elif choice == '4':
            library.update_book_flow()
        elif choice == '5':
            library.delete_book_flow()
        elif choice == '6':
            library.add_user_flow()
        elif choice == '7':
            library.list_users()
        elif choice == '8':
            library.search_user_flow()
        elif choice == '9':
            library.update_user_flow()
        elif choice == '10':
            library.delete_user_flow()
        elif choice == '11':
            library.checkout_book_flow()
        elif choice == '12':
            library.checkin_book_flow()
        elif choice == '13':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")


def main_menu():
    """
    Displays the main menu and returns the user's choice.
    """
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Search Books")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Add User")
    print("7. List Users")
    print("8. Search Users")
    print("9. Update User")
    print("10. Delete User")
    print("11. Checkout Book")
    print("12. Check-in Book")
    print("13. Exit")
    choice = input("Enter choice: ")
    return choice


if __name__ == "__main__":
    main()