print("\033c")

medical=input("did you have a medical cause (y or n) : ")
attendence=int(input("enter the attendence : "))

if medical == "y" :
    print("you are allowed")

else :
    if attendence >= 75 :
        print("you are allowed")
    
    else :
        print("you are not allowed")