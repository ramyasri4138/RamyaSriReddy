def additems(cart):
    itemname=input("enter item name: ")
    itemprice=float(input("enter the price: "))
    cart.append({'name':itemname,'price':itemprice})
    print(f"{itemname} is added")
def viewitems(cart):
    if not cart:
        print("cart empty")
    else:
        for i,item in enumerate(cart,start=1):
            print(f"{i}. {item['name']}-${item['price']}")
def calculateprice(cart):
    total=sum(item['price'] for item in cart)
    print(f"total price:${total}")
def main():
    cart=[]
    while True:
        value=input("enter the function you want to call(1-4)")
        if value=='1':
            additems(cart)
        elif value=='2':
            viewitems(cart)
        elif value=='3':
            calculateprice(cart)
        elif value=='4':
            print("exiting out of loop")
            break
        else:
            print("wrong value")
main()