#Create a function that takes in three arguments (prob, prize, pay) and returns true if prob * prize > pay; otherwise return false.

#To illustrate, profitable_gamble(0.2, 50, 9) should yield true, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.

def profitable_gamble(prob, prize, pay):
    if prob * prize > pay:
        return True
    else:
        return False 
