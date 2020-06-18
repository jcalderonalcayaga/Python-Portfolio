#Python has a logical operator and. The and operator takes two boolean values, and returns True if both values are True.

#Consider a and b:

#a is checked if it is True or False.
#If a is False, False is returned.
#b is checked if it is True or False.
#If b is False, False is returned.
#Otherwise, True is returned (as both a and b are therefore True ).
#The and operator will only return True for True and True.

#Make a function using the and operator.

def And(a, b):
    if a and b == True:
        return True
    else:
        return False
