

def add_item(shopping_list):
    """Add an item to the shopping list."""
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list):
    """Remove an item from the shopping list."""
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def display_list(shopping_list):
    """Display the current shopping list."""
    if shopping_list:
        print("\nCurrent Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("The shopping list is empty.")

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list manager."""
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(shopping_list)
            pass
        elif choice == '2':
            remove_item(shopping_list)
            pass
        elif choice == '3':
            display_list(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()