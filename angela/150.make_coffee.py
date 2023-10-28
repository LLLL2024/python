from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#MenuItem 类属性： - name (str) 饮料的名称。例如“拿铁” - 成本（浮动）饮料的价格。例如 1.5 - 成分（字典） 制作饮料所需的成分和数量。例如{“water”: 100, “coffee”: 16}
# 菜单类方法： - get_items() 以串联字符串的形式返回所有可用菜单项的名称。例如“latte/espresso/cappuccino” - find_drink(order_name)
# 参数 order_name: (str) 饮料订单的名称。按名称搜索特定饮品的菜单。如果存在则返回 MenuItem 对象，否则返回 None。
# CoffeeMaker 类方法： - report() 打印所有资源的报告。例如水：300ml 牛奶：200ml 咖啡：100g - is_resource_sufficient(drink)
# 参数drink：(MenuItem) 要制作的MenuItem 对象。可以点饮料时返回 True，如果成分不足则返回 False。例如真 - make_coffee（订单）
# 参数顺序： (MenuItem) 要制作的 MenuItem 对象。从资源中扣除所需的成分。
# MoneyMachine 类方法： - report() 打印当前利润，例如Money: $0 - make_payment(cost)
# 参数 cost: (float) 饮料的成本。接受付款时返回 True，如果不足则返回 False。例如错误的

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options} ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
           coffee_maker.make_coffee(drink)