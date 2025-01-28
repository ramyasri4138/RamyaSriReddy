def checkbal(bal):
    print("bal: ",bal)
def depmoney(bal):
    money=float(input("how much to deposit: "))
    bal+=money
    print(money,"deposited","balance: ",bal)
    return bal
def withdraw(bal):
    money=float(input("enter the amount to withdrawL: "))
    if money<bal:
        print("insufficient")
    else:
        bal-=money
        print("new balance:",bal)
    return bal


def main():
    bal=1000
    while True:
        print("atm machine")
        choice=int(input("choose options 1.check balance 2.deposit money 3.withdraw money 4.exit"))
        if choice==1:
            checkbal(bal)
        elif choice==2:
            bal=depmoney(bal)
        elif choice==3:
            bal=withdraw(bal)
        elif choice==4:
            print("exiting out of loop")
            break
        else:
            print("invalid choice")
main()