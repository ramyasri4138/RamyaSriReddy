#demonstrating various list operations in python
import array; #not req

# a=array.array()

#1. An empty list
l1=[]
print("1.An empty list: ",l1)

#2.List with four items(index 0 to 3) we can append the items
l2=[0,1,2,3]
print("2. List with four items: ",l2)

#3.nested list
l3=['abc',['def','ghi']]
print("3. A nested list: ",l3)

#4.Creating a list from a string
l4=list('spam') #converts each charcter of string into list items
print("4.list created from string spam ",l4)

#5.create a list from a range of integers
l5=list(range(-4,4))  #list of integers from -4 to 3
print("5.list created from range(-4,4): ",l5)

#6. Accessing an element by index
l6=[10,20,30,40]
print("6.Element at index 2 of l6: ",l6[2])

#7.accessing an element from an nested list by index
l7=['x',[10,20,30],'y']
print("7.Element at l7[1][2] (nested list): ",l7[1][2])

#8.slicing a list
l8=[0,1,2,3,4,5]
print("8. Slicing l8 from index 2 to 4 (l8[2:5]) : ",l8[2:5])

#9.getting the length of a list
print("9.length of l8: ",len(l8))

#10.Demonstrating the nested indexing and slicing together
l9=[10,[100,200,300,400],50]
print("10a. Element at l9[1]: ",l9[1]) #access the sublist
print("10b. Element at l9[1][3]: ",l9[1][3]) # access element 3 from the sublist
print("10c. Slicing sublist l9[1][1:3]: ",l9[1][1:3]) # slice the sublist

#summary of outputs
print("summary of lists: ")
print("l1: ",l1)
print("l2: ",l2)
print("l3: ",l3)
print("l4: ",l4)
print("l5: ",l5)
print("l6: ",l6)
print("l7: ",l7)
print("l8: ",l8)
print("l9: ",l9)