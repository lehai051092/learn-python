from art import logo
import data


def handle_status_machine(choice):
    is_on = True
    is_report = False

    if choice == "off":
        print("The machine turn off.")
        is_on = False
    elif choice == "report":
        is_report = True

    return {"is_on": is_on, "is_report": is_report, "choice": choice}


def handle_show_report(current_resources, money):
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${money}")


def handle_check_resources(current_resources, data_ingredients):
    result = {
        "is_enough": True,
        "resources": []
    }

    if "water" in data_ingredients and current_resources['water'] < data_ingredients['water']:
        result["is_enough"] = False
        result["resources"].append("water")

    if "milk" in data_ingredients and current_resources['milk'] < data_ingredients['milk']:
        result["is_enough"] = False
        result["resources"].append("milk")

    if "coffee" in data_ingredients and current_resources['coffee'] < data_ingredients['coffee']:
        result["is_enough"] = False
        result["resources"].append("coffee")

    return result


def handle_calculate_coins():
    total = 0
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01

    quarters = int(input("Please enter quarters: "))
    total += quarters * quarter

    dimes = int(input("Please enter dimes: "))
    total += dimes * dime

    nickles = int(input("Please enter nickles: "))
    total += nickles * nickel

    pennies = int(input("Please enter pennies: "))
    total += pennies * penny

    return total


def handle_check_transaction(current_money, money, cost):
    money = round(money, 2)
    result = {
        "current_money": round(current_money, 2),
        "refunded": 0,
        "is_enough": True,
    }

    if cost > money:
        result["refunded"] += money
        result["is_enough"] = False
        print(f"Sorry that's not enough money! Money ${result['refunded']} refunded.")
    else:
        result["current_money"] += cost

        if cost < money:
            result["refunded"] += money - cost
            print(f"Too much money! Money ${result['refunded']} refunded.")

    return result


def handle_deducted_resources(current_resources, data_ingredients):
    if "water" in data_ingredients:
        current_resources['water'] -= data_ingredients['water']

    if "milk" in data_ingredients:
        current_resources['milk'] -= data_ingredients['milk']

    if "coffee" in data_ingredients:
        current_resources['coffee'] -= data_ingredients['coffee']

    return current_resources


def start_machine():
    is_completed = False
    current_money = 0
    current_resources = data.resources.copy()
    menu = data.MENU.copy()

    while not is_completed:
        try:
            print(logo)
            status_machine = handle_status_machine(
                input("What would you like? (espresso/latte/cappuccino/report) ").lower())
            is_on = status_machine["is_on"]
            is_report = status_machine["is_report"]
            choice = status_machine["choice"]

            if is_on:

                if choice in ["espresso", "latte", "cappuccino", "report"]:
                    if is_report:
                        handle_show_report(current_resources, current_money)
                    else:
                        result_check_resources = handle_check_resources(current_resources, menu[choice]["ingredients"])
                        if not result_check_resources['is_enough']:
                            print(f"Sorry there is not enough {', '.join(result_check_resources['resources'])}.")
                        else:
                            money = handle_calculate_coins()
                            result_check_transaction = handle_check_transaction(
                                current_money,
                                money,
                                menu[choice]["cost"]
                            )
                            if result_check_transaction["is_enough"]:
                                current_money += result_check_transaction["current_money"]
                                current_resources = handle_deducted_resources(
                                    current_resources,
                                    menu[choice]["ingredients"]
                                )
                                handle_show_report(current_resources, current_money)
                                print(f"Make coffee done! Here is your {choice}. Enjoy!")
                                print("\n" * 20)

                else:
                    print("Input invalid. Please try again.")
            else:
                is_completed = True
        except:
            print("Input invalid. Please try again.")


start_machine()
