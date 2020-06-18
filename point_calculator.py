#Create a function that takes the number of wins, draws and losses and calculates the number
#of points a football team has obtained so far. A win receives 3 points, a draw 1 point and a loss 0 points
def football_points(wins, draws, losses):
    #wins = 3
    #draws = 1
    #losses = 0
    while True:
        if wins > 0 or draws > 0 or losses > 0:
            return ((wins * 3) + (draws * 1) + (losses*0))
        else:
            break
        

                    
	
