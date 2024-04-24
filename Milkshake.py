budget = float(input("Enter your budget: "))

milkshakes = {1: {"flavour": "Vanilla", "price": 3.50}, 2: {"flavour": "Chocolate", "price": 4.00}, 3: {"flavour": "Strawberry", "price": 4.50},}

while True:
    print("Menu:")
    print("1. Vanilla: 3.50")
    print("2. Chocolate: 4.00")
    print("3. Strawberry: 45.0")
    print("Q. Quit")

    choice = input("What Milkshake? (Enter the number of milkshake, or 'Q' to quit): ")

    if choice == 'Q' or 'q':
        print("Ok Bye")
        break

    if choice == '1' or '2' or '3':
        choice = int(choice)
        selected_milkshake = milkshakes[choice]
        if budget >= selected_milkshake['price']:
            print(f"You ordered a {selected_milkshake['flavour']} milkshake.")
            budget -= selected_milkshake['price']
            print(f"Remaining budget: ${budget}")
        else:
            print("you can't afford that.")
            break
    else:
        print("Invalid input! Please enter a number from the menu or 'Q' to quit.")
