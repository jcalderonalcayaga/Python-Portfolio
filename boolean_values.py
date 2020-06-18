#Write a function that returns the strings:

#"both" if both given booleans a and b are True.
#"first" if only a is True.
#"second" if only b is True .
#"neither" if both a and b are False.

def are_true(a,b):
    if a and b == True:
        return 'both'
    elif a == True:
        return 'first'
    elif b == True:
        return 'second'
    elif a or b == False:
        return 'neither' 
    
