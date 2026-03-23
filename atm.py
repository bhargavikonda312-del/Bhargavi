user = 'Bhargavi'
password = '4183'
c_name = input("Enter your name:")
c_pass =str(input("Enter your pass:"))
if c_name == user and c_pass == password:
  amount = 500000
while True:
    print(
        '''''
          1.deposite
          2.check balance
          3.withdraw
          4.mini statement
          5.exit
        '''''
          )
    amount = 500000
    #c_name and c_pass
    #select ooption
    option = int(input("select your option:"))
    if option == 1:
        dep = int(input("Enter the amount"))
        amount+=dep
        print("Total amount :",amount)
    elif option == 2:
        print("Total amount:",amount)
    elif option == 3:
        withd = int(input("Enter the amount:"))
        amount-=withd
        print("Total amount:",amount)
    elif option == 4:
        print("====ATM MINI STATEMENT====")
        print("Username:",user)
        print("Total amount:",amount)
        
    elif option == 5:
      print("Thanks for visiting!")
      break
    else:
        print("please tyr again!")
else:
     print("please enter correct login details")
