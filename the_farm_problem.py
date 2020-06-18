def animals(chickens, cows, pigs):
    
    #In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
    #chickens = 2 legs
    #cows = 4 legs
    #pigs = 4 legs
    #The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.

    while True:
        if chickens > 0 or cows >0 or pigs > 0:
            return (chickens*2) + (cows*4) + (pigs*4)
        else:
            break
