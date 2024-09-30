print ( "\033c" )

print ( "select your ride:" )
print ( "(1) bike" )
print ( "(2) car" )

choice_1 = int ( input ( "enter your choice ( 1 or 2 ) : " ) )

if choice_1 == 1 :
    print ( "\nwhat type of bike?" )
    print ( "(1) motorcycle" )
    print ( "(2) scooter" )

    choice_2 = int ( input ( "enter your choice ( 1 or 2 ) : " ) )
    
    if choice_2 == 1 :
        print ( "\nyou have selected motorcycle" )
    
    elif choice_2 == 2 :
        print ( "\nyou have selected scooter" )
    
    else :
        print ( "\nwrong choice!" )

elif choice_1 == 2 :
    print ( "\nwhat type of car?" )
    print ( "(1) sedan" )
    print ( "(2) SUV" )
    
    choice_3 = int ( input ( "enter your choice ( 1 or 2 ) : " ) )
    
    if choice_3 == 1 :
        print ( "\nyou have selected sedan" )
    
    elif choice_3 == 2 :
        print ( "\nyou have selected SUV" )
    
    else :
        print ( "\nwrong choice!" )

else :
    print ( "\nwrong choice!" )