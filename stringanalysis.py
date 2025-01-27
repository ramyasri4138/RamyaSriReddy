def stringanalysis(userinput):
    vowels='aeiouAEIOU'
    specialchar=r'!@#$%^&*(){}[]:",|\;.'
    vowelcount=0
    consonantcount=0
    specialchars=0
    digitsno=0
    for char in userinput:
        if char.isdigit():
            digitsno+=1
        elif char in vowels:
            vowelcount+=1
        elif char in specialchar:
            specialchars+=1
        elif char.isalpha():
            consonantcount+=1
    reversestring=userinput[::-1]
    print("reverse string is: ",reversestring)        
    print("number of digits is: ",digitsno)
    print("vowel count is: ",vowelcount)
    print("consonant count: ",consonantcount)        
    print("special letter count : ",specialchars)    
    
    
userinput=input("enter the string: ")
stringanalysis(userinput)