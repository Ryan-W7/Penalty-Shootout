import random 
import csv 
#import matplotlib.pyplot as plt

def GameMode():
  print("1. Singleplayer")
  print("2. Multiplayer")
  print("3. Simulation(Computer VS Computer)")
  print("4. Analysis")


Player1Goals = 0
Player2Goals = 0 
Saves = 0 
r = 0

def goals(player): 
  if player == goalkeeper:
    print("Save!")
    Saves + 1
    return 0
  elif player == 'R':
    if  goalkeeper == 'L' or goalkeeper == 'M':
     print("Goal!")
     return 1
  elif player == 'L':
    if  goalkeeper == 'R':
     print("Goal!")
     return 1
  elif player == 'M':
    if  goalkeeper == 'R' or goalkeeper == 'L':
     print("Goal!")
     return 1


def result():
  if Player1Goals > Player2Goals: 
    result = 'player1!'
  elif Player1Goals == Player2Goals:
    result = 'Draw'
  elif Player1Goals < Player2Goals:
    result = 'player2!'

  return result
    
  
  
directions = ("R", "M", "L")


GameMode() 
Mode = input("Choose a mode:") 
while Mode not in ["1", "2", "3", "4"]:
  print("Invalid mode")
  Mode = input("Choose a mode:") 

#Singleplayer
if Mode == '1' or Mode == 'Singleplayer':
  file = open("data.csv", "a")
  fileWrite = csv.writer(file)
  
  for i in range(5):
    player1 = input("[L]eft  [R]ight  [M]iddle, \nShoot: ") 
    goalkeeper = random.choice(directions)
    print("Goalkeeper dived", goalkeeper)

    r = goals(player1)
    if r == 0:
      Saves = Saves + 1
    else:
      Player1Goals = Player1Goals + int(r)
    
    player2 = random.choice(directions)
    print("Player2 shot", player2)
    goalkeeper = random.choice(directions)
    print("Goalkeeper dived", goalkeeper)
    
    r = goals(player2)
    if r == 0:
      Saves = Saves + 1
    else:
      Player2Goals = Player2Goals + r
    
  #result()
  winner = result()
  print("Winner: ", winner)

  fileWrite.writerow(["Singleplayer", Player1Goals, Player2Goals, winner, "Goalkeeper Saves --->", Saves])
  file.close()


#Multiplayer
if Mode == '2' or Mode == 'Multiplayer':
  file = open("data.csv", "a")
  fileWrite = csv.writer(file)
  
  for i in range(5):
    player1 = input("[L]eft  [R]ight  [M]iddle, \nShoot: ") 
    goalkeeper = random.choice(directions)
    print("Goalkeeper dived", goalkeeper)

    r = goals(player1)
    if r == 0:
      Saves = Saves + 1
    else:
      Player1Goals  = Player1Goals + r
    
    player2 = input("[L]eft  [R]ight  [M]iddle, \nShoot: ") 
    goalkeeper = random.choice(directions)
    print("Goalkeeper dived", goalkeeper)
    
    r = goals(player2)
    if r == 0:
      Saves = Saves + 1
    else:
      Player2Goals  = Player2Goals + r
    
  winner = result()
  print("Winner: ", winner)

  fileWrite.writerow(["Multiplayer", Player1Goals, Player2Goals, winner, "Goalkeeper Saves --->", Saves])
  file.close()

    

#Simulation
if Mode == '3' or Mode == "Simulation":
 file = open("data.csv", "a")
 fileWrite = csv.writer(file)

 simulations = int(input("How many simulations would you like to run?: "))

 while simulations.isdigit == False:
   print("Please enter a number")
   simulations = input("How many simulations would you like to run?: ")
   
  
 for i in range(5): 
  player1 = random.choice(directions)
  print("Player1 shot", player1)
  goalkeeper = random.choice(directions)
  print("Goalkeeper dived", goalkeeper)

  r = goals(player1)
  if r == 0:
    Saves = Saves + 1
  else:
    Player1Goals  = Player1Goals + r
    
  player2 = random.choice(directions)
  print("Player2 shot", player2)
  goalkeeper = random.choice(directions)
  print("Goalkeeper dived", goalkeeper)
    
  r = goals(player2)
  if r == 0:
    Saves = Saves + 1
  else:
    Player2Goals  = Player2Goals + r
    
  
 winner = result()
 print("Winner: ", winner)

 fileWrite.writerow(["Simulation", Player1Goals, Player2Goals, winner, "Goalkeeper Saves --->", Saves])
 file.close()


#Analysis
if Mode == '4' or Mode == 'Analysis':
  file = open("data.csv", 'r')
  fileReader = csv.reader(file)

  wins = []
  winner = []
  #GoalsScored = []
  #GoalsSaved = [] 

  for row in fileReader:
    wins.append(row[3])

    if row[3] == 'player1':
      winner.append(row[1])
    elif row[3] == 'player2':
      winner.append(row[2])



  best = max(set(winner), key = winner.count) 

  player1Goals = wins.count("player1")
  player2Goals = wins.count("player2")
  drawAmount = wins.count("Draw")
'''
  X = ["Player1Wins", "PLayer2Wins", "Draws"]
  Y = [player1Goals, Player2Goals, drawAmount]

  plt.bar(X, Y) 
  plt.savefig("graph.png")
'''

print("\n\n\n")
GameMode()
Mode = input("Choose a mode:")


    
      
      
    

  


  