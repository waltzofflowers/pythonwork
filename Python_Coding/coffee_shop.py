MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

#print(MENU["espresso"]["ingredients"]) 

while True:
    
    choice = input("What would you like? (espresso/latte/cappucino):").lower()
    
    if choice == "report":
        for key, value in resources.items():
            if key in ("Water", "Milk"):
                print(f"{key}: {value}ml")
            elif key == "Coffee":
                print(f"{key}: {value}g")
            elif key == "Money":
                print(f"{key}: ${value}")
    elif choice == "exit":
        break
    elif choice in MENU:
        total = 0

        if total < MENU[choice]["cost"]:
            print("Please insert coins.")
            
            quarter = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
        
            total = 0.25 * quarter + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

            if total >= MENU[choice]["cost"]:
                enough_resources = True
                for key, value in MENU[choice]["ingredients"].items():
                    if resources[key] < value:
                        print(f"Sorry there is not enough {key}.")
                        enough_resources = False
                        break

                if enough_resources:
                    for key, value in MENU[choice]["ingredients"].items():
                        resources[key] = resources[key] - value
                        
                    total_after_charge = float(total - MENU[choice]["cost"])
                    print(f"Here is ${total_after_charge} in change.")
                    print(f"Here is your {choice}. Enjoy!")
                    resources["Money"] = total_after_charge
                else:
                    print("Transaction cancelled.Money refunded.")
            else:
                print("Sorry that's not enough money.Money refunded.")
                resources["Money"] = 0
    else:
        print("Invalid choice. Please select espresso, latte, cappucino, report or exist.")