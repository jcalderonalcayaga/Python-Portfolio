#Problem 1
#Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a','b','c']:
        print(i**2) #INDUCING ERROR, STRING CANNOT BE SQUARED
except TypeError:
    print("Type Error. Please input an integer")

#Problem 2
#Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

try:
    x = 5
    y = 0
    z = x/y #INDUCING ERROR, DIVISION BY ZERO IS NOT ACCEPTABLE
except ZeroDivisionError:
    print("Division by zero cannot be accepted")
finally:
    print("All Done!")

#Problem 3
#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.


def ask():
    while True:
        try:
            n1 = int(input("Please enter a number: "))
        except:
            print("Please try again!")
        else:
            break
    print("Your number squared is: ",n1**2)
    
            
        
ask()
