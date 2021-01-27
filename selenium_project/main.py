from dta import get_data
from vis import get_vis
from aut import buy_sell

print("enter the initials of the companies you would want to buy and sell stocks from.")

ta = ['UMHL','MBL']

disp = input("display the charts? Y:Yes|N:No" )
macd = input("use macd indicator to trade? Y:Yes|N:No")

trade = input("would you like to trade?")

if disp == 'Y' or disp == 'y':
    get_vis(ta)

if macd == 'Y' or macd == 'y':
    print(get_data(ta))

if trade == 'Y' or trade == 'y':
    action = input("B:Buy|S:Sell")
    user_name = input("username")
    password = input("password")
    shares = int(input("number of shares"))
    buy_sell(action,user_name,password,shares,ta)
