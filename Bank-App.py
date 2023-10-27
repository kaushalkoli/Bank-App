
#program on Bank-App
balancek_balance():
    print("total balance:",balance)
def deposit(amt):
    global balance
    balance=balance+amt
    print(amt,"Rs.deposit")
def withdraw(amt):
    global balance
    balance=balance-amt
    print(amt,"Rs.withdraw")
while True:
    choice=int(input("\nenter chioce:\n1.deposit cash\t2.withdraw cash:\n2.check balance\t3")
               match choice:
               case 1:
                  print("deposit cassh")
                  d_amt=int(input("enter amount to deposit:"))
                  deposit(d_amt)
                case 2:
                   print("withdraw cash")
                    w_amt=int(input("enter amount to withdraw:"))
                     withdraw(w_amt)
                 case 3:
                     print("check balance")
                      check_balance()
               case 4:
                    print("exiting...")
                    break
                case _:
                    print("invalid choice")
            
