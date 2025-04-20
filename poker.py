from classes.Card import *
from classes.Player import *
import random
import tkinter as tk
from tkinter import *
import pandas as pd

''' 
-TODO-
   
DONE 1. make the titles dynamic, betting cash will decrease cash: $5000
DONE 2. have a river (4th and 5th card)
3. points are added from better cards + pairs, flushed, full house, etc.
DONE 4. multiple players
DONE 5. graphics
6. points are assigned to hands when they are delivered (before the flop line 155)
7. money is distributed   

'''

# create root window
root = Tk()
root.title("TEXAS HOLD 'EM")

# declare GLOBAL variables
ante = 20
bigBlind = 20
smallBlind = 10
pot = 0

images = [] # garbage collector

x = 1000
y = 800
# center of screen / reference for placing everything on screen
cx = x/2
cy = y/2
root.geometry(f'{x}x{y}')

# create table
table = PhotoImage(file = "assets/table.png")
table_image = tk.Label(root, image = table)
table_image.place(x = x/4, y = cy - 100)

###########################################################################################################
#                                             CARDS AND PLAYERS                                           #
###########################################################################################################

# initialize all suits and values
suits = ['HE', 'SP', 'DI', 'CL']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',]

# create a 4x13 2d array deck
deck = [[Card(values[y], suits[x], False, False) for x in range(4)] for y in range(13)]

# initialize players
p1 = Player('Jeffrie',5000)
p2 = Player('Jacqueline',5000)

# PLACEMENT cards TODO:  make real working cards and show them as facing down
place_cards = [1, 2]
for i in range(2):
   place_cards[i] = PhotoImage(file = "assets/card_back.png")
   place_cards_image = tk.Label(root, image = place_cards[i])
   place_cards_image.place(x = x/4 - 20 + i*54, y = cy)

###########################################################################################################
#                                         ALL DYNAMIC VARIABLES                                           #
###########################################################################################################

# Create Dyanamic Player 1 Cash Variable
p1_cash_dynamic = tk.StringVar()
p1_cash_dynamic.set(f"${p1.cash}")

p1_cash_label = Label(root,textvariable = p1_cash_dynamic)
p1_cash_label.place(x = cx + 60, y = cy + 100)

# Create Dyanamic Player 2 Cash Variable
p2_cash_dynamic = tk.StringVar()
p2_cash_dynamic.set(f"${p2.cash}")

p2_cash_label = Label(root,textvariable = p2_cash_dynamic)
p2_cash_label.place(x = cx + 280, y = cy - 90)

# Create Dynamoc Pot Variable
pot_dynamic = tk.StringVar()
pot_dynamic.set(f"Pot: ${pot}") 

pot_label = Label(root, textvariable = pot_dynamic)
pot_label.place(x = cx, y = cy - 120)

###########################################################################################################
#                                             BETTING MONEY                                               #
###########################################################################################################
# TODO: work on money system

def call(Player):
   # subtract from cash label
   global pot
   if(Player.cash - ante < 0): # TODO replace ante with bet amount 
      print('not enough monies')
   else:
      Player.cash = Player.cash - ante
      # this is really bad. fix
      if(Player == p1):
         p1_cash_dynamic.set(f"${Player.cash}")
      elif(Player == p2):
         p2_cash_dynamic.set(f"${Player.cash}")  
          
      # add to pot TODO change ante to bet amount
      pot = pot + ante
      pot_dynamic.set(f"Pot: ${pot}")

# bet button p1
p1bet_button = Button(root, text = f"P1 Bet ${ante}", command = lambda: call(p1))
p1bet_button.place(x = cx, y = cy + 70)

# bet button p2
p2bet_button = Button(root, text = f"P2 Bet ${ante}", command = lambda: call(p2))
p2bet_button.place(x = cx + 225, y = cy - 120)

###########################################################################################################
#                                               PLAYER HANDS                                              #
###########################################################################################################

# print p1 hand
p1h1v = random.randrange(1,13) # player 1 hand 1 value
p1h1s = random.randrange(1,4)

deck[p1h1v][p1h1s].played = True # initialize that card played to "True"

p1h2v = random.randrange(1,13)
p1h2s = random.randrange(1,4)
while deck[p1h2v][p1h2s].played: # checks on the offchance the card has already been played
   p1h2v = random.randrange(1,13)
   p1h2s = random.randrange(1,4)

# set card at deck to true
deck[p1h2v][p1h2s].played = True

# addCard to player hand
p1.addCard(p1h1v, p1h1s, p1h2v, p1h2s, deck)

# Assign points to hand
   #TODO assign the points

# Load image of hand 
p1hand1 = PhotoImage(file = f"assets/{deck[p1h1v][p1h1s].val}_{deck[p1h1v][p1h1s].suit}.png")
p1hand2 = PhotoImage(file = f"assets/{deck[p1h2v][p1h2s].val}_{deck[p1h2v][p1h2s].suit}.png")

# Display hand on screen
p1hand1_label = tk.Label(root, image = p1hand1)
p1hand1_label.place(x = cx - 54, y = cy + 100)
p1hand2_label = tk.Label(root, image = p1hand2)
p1hand2_label.place(x = cx, y = cy + 100)


# print p2 hand
p2h1v = random.randrange(1,13)
p2h1s = random.randrange(1,4)

deck[p2h1v][p2h1s].played = True # initialize that card played to "True"

p2h2v = random.randrange(1,13)
p2h2s = random.randrange(1,4)
while(deck[p2h2v][p2h2s].played == True): # checks on the offchance the card has already been played 
   p2h2v = random.randrange(1,13)
   p2h2s = random.randrange(1,4)

deck[p2h2v][p2h2s].played = True


p2.addCard(p2h1v, p2h1s, p2h2v, p2h2s, deck)

# Load image of hand 
p2hand1 = PhotoImage(file = f"assets/{deck[p2h1v][p2h1s].val}_{deck[p2h1v][p2h1s].suit}.png")
p2hand2 = PhotoImage(file = f"assets/{deck[p2h2v][p2h2s].val}_{deck[p2h2v][p2h2s].suit}.png")

# Display hand on screen
p2hand1_label = tk.Label(root, image = p2hand1)
p2hand1_label.place(x = cx + 171, y = cy - 90) # 54 pixels away
p2hand2_label = tk.Label(root, image = p2hand2)
p2hand2_label.place(x = cx + 225, y = cy - 90)

###########################################################################################################
#                                         FLOP, TURN, RIVER (BOARD)                                       #
###########################################################################################################

# print the FLOP
flop = ['', '', ''] # array of images
def print_flop():
   for i in range(3):
      f1v = random.randrange(1,13)
      f1s = random.randrange(1,4)
      while deck[f1v][f1s].played: # checks on the offchance the card has already been played
         f1v = random.randrange(1,13)
         f1s = random.randrange(1,4)
      
      deck[f1v][f1s].played = True
      deck[f1v][f1s].board = True
      
      flop[i] = PhotoImage(file = f"assets/{deck[f1v][f1s].val}_{deck[f1v][f1s].suit}.png")
      flop_image = tk.Label(root, image = flop[i])
      flop_image.place(x = cx - 150 + (i * 54), y = cy - 80)

# button to print the FLOP   
flop_button = Button(root, text = f"Print the FLOP", command = print_flop)
flop_button.place(x = cx - 118, y = cy + 20)

# print the TURN           
def print_turn():
   # print one more card to the fuckin thing
   turnV = random.randrange(1,13)
   turnS = random.randrange(1,4)
   while(deck[turnV][turnS].played == True): # checks on the offchance the card has already been played 
      turnV = random.randrange(1,13)
      turnS = random.randrange(1,4)
   
   deck[turnV][turnS].played = True
   deck[turnV][turnS].board = True
   
   turn = PhotoImage(file = f"assets/{deck[turnV][turnS].val}_{deck[turnV][turnS].suit}.png")
   images.append(turn) # throw image into garbage bin
   turn_image = tk.Label(root, image = turn)
   turn_image.place(x = cx - 150 + (3 * 54), y = cy - 80) # 3 * because it is after the FLOP
   
# button to print the TURN   
turn_button = Button(root, text = f"Print the TURN", command = print_turn)
turn_button.place(x = cx - 30, y = cy + 20)

# print the RIVER
def print_river():
   # print one more card to the fuckin thing
   riverV = random.randrange(1,13)
   riverS = random.randrange(1,4)
   while deck[riverV][riverS].played == True: # checks on the offchance the card has already been played
      riverV = random.randrange(1,13)
      riverS = random.randrange(1,4)
   
   deck[riverV][riverS].played = True
   deck[riverV][riverS].board = True
   
   river = PhotoImage(file = f"assets/{deck[riverV][riverS].val}_{deck[riverV][riverS].suit}.png")
   images.append(river) # throw image into garbage bin
   river_image = tk.Label(root, image = river)
   river_image.place(x = cx - 150 + (4 * 54), y = cy - 80) # 4 * because it is after the TURN
   
# button to print the RIVER   
river_button = Button(root, text = f"Print the RIVER", command = print_river)
river_button.place(x = cx + 60, y = cy + 20)  

def print_deck(deck):
   # Create lists to store deck information
   values = []
   suits = []
   board_status = []
   played_status = []

   # Iterate through the deck and collect information
   for v in range(13):
      for s in range(4):
         values.append(deck[v][s].val)
         suits.append(deck[v][s].suit)
         board_status.append('On Board' if deck[v][s].board else 'Not on Board')
         played_status.append('Played' if deck[v][s].played else 'Not Played')

   # Create a DataFrame
   df = pd.DataFrame({
      'Value': values,
      'Suit': suits,
      'Board Status': board_status,
      'Played Status': played_status
   })

   # Print the DataFrame
   print(df)


points_button = Button(root, text = f"Show Player 1 Stats", command = lambda: p1.getInfo(deck))
points_button.place(x = 0, y = 0)

points2_button = Button(root, text = f"Show Player 2 Stats", command = lambda: p2.getInfo(deck))
points2_button.place(x = 0, y = 30)

print_deck_button = Button(root, text = f"Print Deck to Terminal", command = lambda: print_deck(deck))
print_deck_button.place(x = 0, y = 60)

calc_strength_button = Button(root, text = f"Calculate Player 1 Strength", command = lambda: p1.calc_Strength(deck))
calc_strength_button.place(x = 120, y = 0)

calc_strength_button2 = Button(root, text = f"Calculate Player 2 Strength", command = lambda: p2.calc_Strength(deck))
calc_strength_button2.place(x = 120, y = 30)


# Execute Poker
root.mainloop()