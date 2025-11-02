from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_working = True
beverage_available = menu.get_items()

while(is_working):
  beverage_name = input(f'What beverage would you like? ({beverage_available})\n')
  if beverage_name == 'off':
    is_working = False
  elif beverage_name == 'report':
    coffee_machine.report()
    money_machine.report()
  else: 
    beverage = menu.find_drink(beverage_name)
    if beverage and coffee_machine.is_resource_sufficient(beverage):
      if money_machine.make_payment(beverage.cost):
        coffee_machine.make_coffee(beverage)


