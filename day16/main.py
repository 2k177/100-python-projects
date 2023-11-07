from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
# menu_item_obj = MenuItem()
coffee_maker_obj = CoffeeMaker() 
money_machine_obj = MoneyMachine()

user_choice = input("Could you please order ?? (latte/espresso/cappuccino/report)")

if user_choice.lower() == "report":
  coffee_maker_obj.report()
  money_machine_obj.report()
else:
  status = coffee_maker_obj.is_resource_sufficient(Menu().find_drink(user_choice))
  print(status)

  if status == True:
    drink_cost = menu_obj.find_drink(user_choice).cost
    print(f"Please pay {menu_obj.find_drink(user_choice).cost}.")
    money_transaction = money_machine_obj.make_payment(drink_cost)
    if money_transaction:
      print("Your transaction is successfull !!")
      coffee_maker_obj.make_coffee(menu_obj.find_drink(user_choice))
      
    else:
      print("Transaction failed, Sorry !!")

