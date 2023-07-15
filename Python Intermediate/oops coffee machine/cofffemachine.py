MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def choice(user_input):
    """ store the value of function coffe in a variable and execute further acoording to that varile and update
    resouces dict. """

    a = coffee(quaters_coins, dimes_coin, nickles_coin, pennies_coin)
    if a:
        if user_input == "espresso":
            resources["water"] = resources["water"] - MENU[user_input]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[user_input]["ingredients"]["coffee"]
            resources["Money"] = MENU[user_input]["cost"]
        else:
            resources["water"] = resources["water"] - MENU[user_input]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU[user_input]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU[user_input]["ingredients"]["coffee"]
            resources["Money"] = MENU[user_input]["cost"]
        
        print(f'Here is your {user_input}. Enjoy!')
    else:
        print("Sorry that's not enough money. Money Refunded.")

    
def coffee(quaters_coins, dimes_coin, nickles_coin, pennies_coin):
    """ Calculate the monetary value. if monetary value is less than cost of drink it returns false
    otherwise calculate and print change and return true"""

    
    if user_input == "espresso":
        monetary_value = 0.25*quaters_coins + 0.1* dimes_coin + 0.05*nickles_coin + 0.01*pennies_coin
    if user_input == "latte":
        monetary_value = 0.25*quaters_coins + 0.1* dimes_coin + 0.05*nickles_coin + 0.01*pennies_coin
    if user_input == "cappuccino":
        monetary_value = 0.25*quaters_coins + 0.1* dimes_coin + 0.05*nickles_coin + 0.01*pennies_coin

    if monetary_value < MENU[user_input]["cost"]:
           return False
    
    change =(monetary_value -  MENU["latte"]["cost"])
    print (f"Here is ${round(change, 2)} in change")
    return True


def report ():
    """ Gives available resources """

    print(f' Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["Money"]}')

def ingredients():
    """ Check for ingrdients required to make a drink. """

    for ingredient in resources:
            for ingredient in  MENU[user_input]["ingredients"]:
                if resources[ingredient] < MENU[user_input]["ingredients"][ingredient]:
                    print(f"sorry ther is not enough {ingredient}")
                    return False
                else:
                    return True
    
    
coffe_machine = True
while coffe_machine:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "espresso" or user_input ==  "latte" or user_input ==  "cappuccino" :  
        if ingredients() is True:
            print("Please insert coins")
            quaters_coins = int(input("How many quarters? :"))
            dimes_coin = int(input("How many dimes?: "))  
            nickles_coin = int(input(" How many nickles? :"))     
            pennies_coin = int(input(" How many pennies?: "))         
            choice(user_input)    

    elif user_input == "off":
        break
   
    elif user_input == "report":
      report()

    else:
        print("Invalid input")
        break
 
