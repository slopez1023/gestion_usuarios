from UserManager import register_user, update_user,delete_user
from ProductManager import add_product,update_product,delete_product

def main_menu():
    print("Welcome to the Te lo consigo platform!")
    print("1. Manage users")
    print("2. Manage products")
    print("3. Exit")

def user_menu():
    print("User management menu")
    print("1. Register user")
    print("2. Update user")
    print("3. Delete user")
    print("4. Back to main menu")

def product_menu():
    print("Product management menu")
    print("1. Add product")
    print("2. Update product")
    print("3. Delete product")
    print("4. Back to main menu")

def main():
    while True:
        main_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            while True:
                user_menu()
                sub_choice = int(input("Enter your choice: "))
                if sub_choice == 1:
                    register_user()
                elif sub_choice == 2:
                    update_user()
                elif sub_choice == 3:
                    delete_user()
                elif sub_choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == 2:
            while True:
                product_menu()
                sub_choice = int(input("Enter your choice: "))
                if sub_choice == 1:
                    add_product()
                elif sub_choice == 2:
                    update_product()
                elif sub_choice == 3:
                    delete_product()
                elif sub_choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()