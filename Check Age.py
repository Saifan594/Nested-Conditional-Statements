print("\033c")

# initializing variables
age = input ( "enter your age : " )
age = int ( age )

# checking age
if age < 10 :
    print ( "you are too young for this class" )

elif age > 20 :
    print ( "you are too old for this class" )

else :
    print ( "you can do this class" )