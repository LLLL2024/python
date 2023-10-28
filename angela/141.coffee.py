#1.通过询问“您想要什么？ （浓缩咖啡/拿铁/卡布奇诺）：”检查用户的输入以决定下一步做什么。湾。提示应在每次操作完成时显示，例如一旦饮料被分配。提示应再次显示以服务下一位客户。
#2.在提示符下输入“off”关闭咖啡机。一个。对于咖啡机的维护者来说，他们可以使用“关闭”作为关闭机器的密码。发生这种情况时，您的代码应该结束执行。
#3.打印报告。一个。当用户在提示中输入“report”时，应该生成一个显示当前资源值的报告。例如水：100ml 牛奶：50ml 咖啡：76g 金钱：2.5 美元
#4. 检查资源是否充足？一个。当用户选择一种饮料时，程序应该检查是否有足够的资源来制作这种饮料。湾。例如。如果拿铁需要 200 毫升水，但机器中只剩下 100 毫升。它不应该继续制作饮料，而是打印：“对不起，水不够。” C。如果另一个资源耗尽，也会发生同样的情况，例如牛奶或咖啡。
#5.处理硬币。一个。如果有足够的资源来选择饮料，那么程序应该提示用户投入硬币。湾。请记住，硬币 = 0.25 美元，硬币 = 0.10 美元，镍币 = 0.05 美元，便士 = 0.01 美元 c。计算插入硬币的货币价值。例如。 1 季度，2 硬币，1 镍，2 便士 = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
#6.检查交易是否成功？一个。检查用户是否投入了足够的钱来购买他们选择的饮料。例如，拿铁咖啡售价 2.50 美元，但他们只插入了 0.52 美元，然后在数完硬币后，程序应该说“对不起，钱不够。钱退了。”湾。但是如果用户投入了足够的钱，那么饮料的成本就会作为利润添加到机器中，这将在下次触发“报告”时反映出来。例如。水：100ml 牛奶：50ml 咖啡：76g 金钱：2.5 美元 c.如果用户投入了太多钱，机器应该提供零钱。
#例如。 “这是 2.45 美元的零钱。”更改应四舍五入到小数点后 2 位。 7. 煮咖啡。一个。如果交易成功并且有足够的资源来制作用户选择的饮品，那么制作饮品的原料应该从咖啡机资源中扣除。例如。购买拿铁前报告： 水：300ml 牛奶：200ml 咖啡：100g 金钱：$0 购买拿铁后报告： 水：100ml 牛奶：50ml 咖啡：76g 金钱：$2.5 b.扣除所有资源后，告诉用户“这是你的拿铁咖啡。享受！”。如果拿铁咖啡是他们选择的饮料。
from main import MENU
drink = input("What would you like?  espresso/latte/cappuccino: ")

machine_Water = 300
machine_coffee = 100
machine_milk = 200
machine_money = 0
successful = False
should_coffee = False
cost = "cost"


def Process_coins():
    quarters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickles = int(input("how many nickles?"))
    pennis = int(input("how many pennis?"))
    coins = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennis * 0.01
    cost_coins = MENU[drink]['cost']
    print(f"{cost_coins}")

    if coins > cost_coins:
       change_money = coins - cost_coins
       successful = True
       print(f"Here is ${change_money} in  change")


    else:
       return "sorrry,that's not enough money.Money refunded "



def check_resources_sufficient():
    if drink == "report":
        print(f"water:{machine_Water}/coffee:{machine_coffee}/money:{machine_money}")

    elif  drink == "latte" or drink == "cappucino":
        remaining_water =  machine_Water - int(MENU[drink]['water'])
        remaining_coffee = machine_coffee -int(MENU[drink]['coffee'])
        remaining_milk = machine_milk - int(MENU[drink]['milk'])
        if remaining_water > 0 or remaining_coffee > 0 or remaining_milk > 0:
            should_coffee= True
            while should_coffee:
                print("please insert coins")
                Process_coins()

    elif drink  == "espresso":
        remaining_water = machine_Water - int(MENU[drink]['water'])
        remaining_coffee = machine_coffee - int(MENU[drink]['coffee'])

        if remaining_water > 0 or remaining_coffee > 0 :
            should_coffee = True
            while should_coffee:
                print("please insert coins")
                Process_coins()


        else:
            return "sorry, there is not enough"




