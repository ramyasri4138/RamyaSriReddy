def celtofah(cel):
    return (cel* 9/5)+32
def fahtocel(fah):
    return (fah-32)*5/9
def celtokel(cel):
    return cel+273
def keltocel(kel):
    return kel-273
def fahtokel(fah):
    return (f-32)*(5/9)+273
def keltofah(kel):
    return (kel-273)*(9/5)+32

def main():
    print("enter options from 1 to 6: ")
    print("1 for celtofah\n 2 for fahtocel\n 3 for celtokel\n 4 for keltocel\n5 for fahtokel\n 6 for keltofah\n7 for exit\n ")
    while True:
        temp=float(input("enter temperature: "))
        choice=input("enter your choice: ")
        if choice =='1':
            print(f"{temp}celsius={celtofah(temp)}fahrenheit")
        elif choice =='2':
            print(f"{temp}fahrenheit = {fahtocel(temp)}celsius")
        elif choice=='3':
            print(f"{temp}celsius={celtokel(temp)}kelvin")
        elif choice=='4':
            print(f"{temp}kelvin= {keltocel(temp)}celsius")
        elif choice=='5':
            print(f"{temp}fahrenheit={fahtokel(temp)}kelvin")
        elif choice=='6':
            print(f"{temp}kel={keltofah(temp)}fahrenheit")
        elif choice=='7':
            print("exiting")
            break
        else:
            print("choice incorrect")
main()