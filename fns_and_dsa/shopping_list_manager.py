def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            input_item = input("Enter the item to add: ")
            shopping_list.append(input_item)
            print(f"{input_item} added to the shopping list.")
        elif choice == '2':
            input_item = input("Enter the item to remove: ")
            if input_item in shopping_list:
                shopping_list.remove(input_item)
                print(f"{input_item} removed from the shopping list.")
            else:
                print(f"{input_item} not found in the shopping list.")
        elif choice == '3':
            print("Shopping List:")
            for item in shopping_list:
                print("- " + item)
            if not shopping_list:
                print("The shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
