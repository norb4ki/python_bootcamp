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


# TODO-1 Ask user which beverage he wants
def validated_input(prompt):
  global resources
  """Takes an user input. Shows report on user command"""
  answer = input(prompt)

  if answer == 'report':
    print_report(resources)
    answer = validated_input(prompt)
  else:
    return answer

def get_beverage(menu):
  """Takes and returns a beverage that exists in menu list from user input. """
  beverage_list = menu.keys()
  beverage = validated_input("What would you like? (espresso/latte/cappucino) ")
  if beverage not in beverage_list and beverage != 'off':
    print("We dont serve this, try again.")
    beverage = get_beverage(menu)
  
  return beverage

def print_report(resources):
  print(f"Water: {resources["water"]}ml")
  print(f"Milk: {resources["milk"]}ml")
  print(f"Coffee: {resources["coffee"]}g")
  try:
    print(f"Money: ${resources["money"]}")
  except KeyError:
    resources["money"] = 0
    print(f"Money: ${resources["money"]}")


def get_payment():
  """Takes coin amount as user input, returns total cash value in $ as float number"""
  try:
    quarters = int(validated_input("How many quarters? "))
    dimes = int(validated_input("How many dimes? "))
    nickles = int(validated_input("How many nickles? "))
    pennies = int(validated_input("How many pennies? "))
  except TypeError:
    print("Try again with whole numbers")

  total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
  return total

def process_payment(money_recieved, money_required, resources):
  if money_recieved >= money_required:
    try:
      resources["money"] += money_required
    except KeyError:
      resources["money"] = 0
      resources["money"] += money_required
      
    change = money_recieved - money_required
    print(f"Here is your change: ${change}")
    return True
  
  else:
    print("Sorry that's not enough money. Money refunded")
    return False
  
def check_recources(resources, beverage):
  ingridients = beverage["ingredients"]
  ingridient_keys = ingridients.keys()
  for key in ingridient_keys:
    if resources[key] < ingridients[key]:
      print (f"Sorry, there is not enough {key}.")
      return False
  
  return True

def make_beverage(resources, beverage):
  print(resources, beverage)

def start():
  beverage_name = get_beverage(MENU)
  if beverage_name == "off":
    return
  beverage = MENU[beverage_name]
  money_recieved = get_payment()
  if check_recources(resources, beverage) and process_payment(money_recieved, beverage["cost"], resources):
    make_beverage(resources, beverage)

  start()
  
  
start()
# TODO-2 Turn off the Coffee Machine
# TODO-3 Print report
# TODO-4 Check is there is enough recources
# TODO-5 Process coins
# TODO-6 Check transaction successful
# TODO-7 Make coffee