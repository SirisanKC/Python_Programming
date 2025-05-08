def display_menu():
    print("You can choose from the functions below:")
    print("1) Add")
    print("2) Remove")
    print("0) End")

def shopping_list():
    shopping_list = []
    while True:
        print("Your shopping list contains the following products:")
        print(shopping_list)
        display_menu()
        choice = input("Your choice:\n")
        
        if choice == '1':
            product = input("Enter the product to be added:\n")
            print()
            shopping_list.append(product)
        elif choice == '2':
            if len(shopping_list) == 0:
                print("Your shopping list is empty, nothing to remove.")
            else:
                print(f"You have {len(shopping_list)} items in your shopping list.")
                try:
                    index = int(input("Enter the location of the product to be removed:\n")) - 1
                    print()
                    if 0 <= index < len(shopping_list):
                        shopping_list.pop(index)
                    else:
                        print("Invalid location.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == '0':
            print("You are going to buy the following products:")
            print(shopping_list)
            break
        else:
            print("Unknown selection.")
            print()
shopping_list()