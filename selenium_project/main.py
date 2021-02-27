from dta import get_data
from vis import get_vis
from aut import buy_sell

print("enter the initials of the companies you would want to buy and sell stocks from.")

ta = ['UMHL','MBL']

disp = input("display the charts? Y:Yes|N:No" )

if disp == 'Y' or disp == 'y':
    get_vis(ta)

macd = input("use macd indicator to trade? Y:Yes|N:No")    
    
if macd == 'Y' or macd == 'y':
    print(get_data(ta))
    

trade = input("would you like to trade?")

if trade == 'Y' or trade == 'y':
    action = input("Buy:Buy|Sell:Sell")
    user_name = input("username")
    password = input("password")
    shares = int(input("number of shares"))
    
    
    # buy_sell(action,user_name,password,shares,ta) --> this function has not been defined with shares and ta. 
    
