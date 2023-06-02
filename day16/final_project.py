from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like to order: ({options}): ')

    if choice == 'off':
        print('Thanks for using our service. 😀')
        is_on = False
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            # print(drink)
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)