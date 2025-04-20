class Card:
   def __init__(self, val, suit, played, board): # val = value
      self.val = val
      self.suit = suit 
      self.played = played # if the card is played (either on the board or on the BOARD)
      self.board = board   # if the card is on the board (FLOP, TURN, RIVER)
      
   def getSuit(self):
      return self.suit
      
   def getVal(self):
      return self.val
        
   def __str__(self):
      return f'{self.val}_{self.suit}'