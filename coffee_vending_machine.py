import time

menu = {
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee powder":20,
            "sugar":50
        },
        "cost":100
    },
    "espresso":{
        "ingredients":{
            "water":150,
            "coffee powder":20,
            "sugar":50
        },
        "cost":200
    },
    "cappuccino":{
        "ingredients":{
            "water":150,
            "milk":200,
            "coffee powder":50,
            "sugar":35,
        },
        "cost":350
    }
}




profit = 0
coffee_ingredients = {
    "water":500,
    "milk":200,
    "coffee powder":80,
    "sugar":150
}


def check_ingre(order_ingre):
    for item in order_ingre:
        if order_ingre[item] > coffee_ingredients[item]:
            print(f"Sorry insufficient ingredients of {item}")
            print("\nType 'report' to see ingredients balance or Type 'off' to exit(report/off)...")

            return False
    return True

def process_coins():
    print("Please insert coins: ")
    total = 0
    coin_five = int(input("How many five rs coins? \n"))
    coin_ten = int(input("How many ten rs coins? \n"))
    coin_twenty = int(input("How many twenty rs coins? \n"))
    total = coin_five*5 + coin_ten*10 + coin_twenty*20
    return total

def payment_success(money_received,cof_cost):
    if money_received>=cof_cost:
        global profit
        profit += cof_cost
        change = money_received - cof_cost
        print(f"Here is your Rs {change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    print("\nType 'report' to see ingredients balance or Type 'off' to exit(report/off)...")


def make_coffee(cof_name,cof_ingre):
    for item in cof_ingre:
        coffee_ingredients[item] -= cof_ingre[item]
    print(f"Here is your {cof_name}... Enjoy!!! ")
    print("\nType 'report' to see ingredients balance or Type 'off' to exit(report/off)...")

flag = True
while flag:
    user_choice = input("What is your favourite? (latte, espresso, cappuccino)\n").lower()
    if user_choice == 'off':
        flag = False
        print("Coffee machine turned off!!")
    elif user_choice == 'report':
        print(f"Water: {coffee_ingredients['water']}ml")
        print((f"Milk: {coffee_ingredients['milk']} ml"))
        print((f"Coffee powder: {coffee_ingredients['coffee powder']} g"))
        print((f"Sugar: {coffee_ingredients['sugar']} g"))
        print(f"Money: Rs {profit}")
        print("\nType 'report' to see ingredients balance or Type 'off' to exit(report/off)...")

    else:
        coffee_type = menu[user_choice]
        #print(coffee_type)
        if check_ingre(coffee_type['ingredients']):
            payment = process_coins()
            if payment_success(payment,coffee_type['cost']):
                make_coffee(user_choice, coffee_type['ingredients'])

time.sleep(5)