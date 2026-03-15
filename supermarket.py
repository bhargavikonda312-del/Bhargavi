from datetime import datetime
name = input("Enter you name:")
# LISTS of items
lists = '''
rice    : 20
sugar   : 30
oil     : 50
maggi   : 20
colgate : 80
'''
# Declaration
price = 0
pricelist = []
totalprice = 0
finalamount = 0
ilist = []
qlist = []
plist = []
# rates for items
items = {'rice': 20, 'sugar': 30, 'oil': 50, 'maggi': 20, 'colgate': 80}
OPtion = int(input("for list of items press 1:"))
if OPtion == 1:
    print(lists)
while True:
    inp = int(input("If You want to buy press 1 or 2 for exit:"))
    if inp == 2:
        break
    if inp == 1:
        item = input("Enter your items:")
        quantity = int(input("Enter quantity:"))
        if item in items.keys():
            price = quantity * items[item]
            pricelist.append([item, quantity, items[item], price])
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp = input("can:bill the items yes or no: ")
    if inp.lower() == "yes" :
        print(25 * "-", "Bharagvi supermarket", 25 * "-")
        print(28 * " ", "wanaparthy")
        print("Name:", name, 30 * " ", "Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(75 * "-")
        print("sno", 8 * " ", 'Item', 8 * "   ", 'Quantity', 10 * "  ", 'Price')
        for i in range(len(pricelist)):
            print(i + 1, 10 * " ", pricelist[i][0], 8 * "   ", pricelist[i][1], 8 * "   ", pricelist[i][3])
        print(35 * "-")
        print(50 * "  ", 'totalamount:', 'rs', +totalprice)
        print(50 * "-")
        print("gst amount", 40 * " ", 'rs',)
        print(75 * "- ")
        print(50 * " ", 'finalamount:', 'rs', finalamount)
        print(75 * "- ")
        print(20 * "  ", "thanks for visiting")

        print(75 * "- ")
 