class Player:
   board_hand_val = ['0', '0', '0', '0', '0', '0', '0']
   board_hand_suit = ['00', '00', '00', '00', '00', '00', '00']
   def __init__(self, name, cash, strength = 0, points = 0, hand_values = None, hand_suits = None):
      self.name = name
      self.cash = cash
      self.strength = strength  # list in Hand-Ranking categories
      self.points = points  # how strong player's hand is based on points of value of card
                           # if two players have the same amount of points, it is a tie

      # Initialize hand_values and hand_suits as lists with two elements if not provided
      self.hand_values = hand_values if hand_values is not None else ['', '']
      self.hand_suits = hand_suits if hand_suits is not None else ['', '']

   # accessor variables
   def __str__(self):
      return self.name
   def getCash(self):
      return self.cash
   def getStrength(self):
      return self.strength
   def getPoints(self):
      return self.points
   def getHandValues(self):
      return self.hand_values[0], self.hand_values[1]
   def getHandSuits(self):
      return self.hand_suits[0], self.hand_suits[1]

   def setStrength(self, int):
      self.strength = int

   # add the card to the player's hand
   def addCard(self, h1v, h1s, h2v, h2s, deck):

      # Make the hand_suits and hand_values = the card instead of the index
      cardOne = deck[h1v][h1s]
      cardTwo = deck[h2v][h2s]

      self.hand_suits[0] = cardOne.getSuit()
      self.hand_suits[1] = cardTwo.getSuit()

      self.hand_values[0] = cardOne.getVal()
      self.hand_values[1] = cardTwo.getVal()

   def calc_points(self):
      total = 0
      # make card points equal number value in deck
      for i in range(2):
         if self.hand_values[i] == 'J':
            cardPoints = 11
         elif self.hand_values[i] == 'Q':
            cardPoints = 12
         elif self.hand_values[i] == 'K':
            cardPoints = 13
         else:
            cardPoints = int(self.hand_values[i])  # parse str to int
         # total the points
         total = total + cardPoints

      # player's points assigned to player
      self.points = total

   def calc_Strength(self, deck):
      self.getInfo(deck)
      # Calculate the strength of a players hand using a list of different combos you can have
      '''
      1 - Royal Flush
      2 - Straight Flush
      3 - Four of a Kind
      4 - Full House
      5 - Flush
      6 - Straight
      7 - Three of a Kind
      8 - Two Pair
      9 - Pair
      1 - High Card - Go by highest points
      '''
      # can only have max of two pair groups (pair, two pair, 3/4 of a kind, full house)
      # First, sort the hand values
      sorted_hand = sorted(self.board_hand_val)

      # Count occurrences of each card value
      value_counts = {}
      for value in sorted_hand:
         if value in value_counts:
            value_counts[value] += 1
         else:
            value_counts[value] = 1

      # Find groups of cards (pairs, three of a kind, etc.)
      pairs = []
      three_of_a_kind = []
      four_of_a_kind = []

      for value, count in value_counts.items():
         if count == 2:
            pairs.append(value)
         elif count == 3:
            three_of_a_kind.append(value)
         elif count == 4:
            four_of_a_kind.append(value)

      print(f'Pairs: {pairs}')
      print(f'Three of kind: {three_of_a_kind}')
      print(f'Four of kind: {four_of_a_kind}')
      print('-----------------------------------')

      '''
            1 - Royal Flush
            2 - Straight Flush
            3 - Four of a Kind
            4 - Full House
            5 - Flush
            6 - Straight
            7 - Three of a Kind
            8 - Two Pair
            9 - Pair
            1 - High Card - Go by highest points
      '''
      # IF THERE IS AT LEAST ONE PAIR - when only flop is played, both players will
      # have a pair of 0 for the cards not on screen. If this breaks, check and possibly fix
      if pairs:
         self.setStrength(1)
      # TWO PAIR - take into account of having 3 pairs
      if len(pairs) >= 2:
         self.setStrength(2)
      # THREE OF A KIND
      if three_of_a_kind:
         self.setStrength(3)
      # STRAIGHT
      # FLUSH
      # FULL HOUSE - if player has either two Three_of_a_kind or a Three_of_a_kind and a pair
      if len(three_of_a_kind) == 2 or (len(three_of_a_kind) >= 1 and pairs):
         self.setStrength(6)
      # FOUR OF A KIND
      if four_of_a_kind:  # check to see if there is anything in four_of_a_kind
         self.setStrength(7)
      # add royal flush + straight flush

      print('Strength:',self.getStrength())

      return 0

   def getInfo(self,deck):
      # last two cards are the ones in your hand
      board_hand_val = ['0', '0', '0', '0', '0', f'{self.hand_values[0]}', f'{self.hand_values[1]}']
      board_hand_suit = ['00', '00', '00', '00', '00', f'{self.hand_suits[0]}', f'{self.hand_suits[1]}']

      # iterate over the deck
      for v in range(13):
         for s in range(4):
            # if one the card is on the board
            if deck[v][s].board:
               # add i to the array
               for i in range(5):
                  if board_hand_val[i] == '0':
                     board_hand_val[i] = deck[v][s].val
                     board_hand_suit[i] = deck[v][s].suit
                     break
      # set the board hand value and board hand suits to the array in class to be used elsewhere
      self.board_hand_val = board_hand_val
      self.board_hand_suit = board_hand_suit

      # calculate points
      self.calc_points()
      print(f'{self.name}\'s Points: {self.getPoints()}')
      print(f'{board_hand_val}\n{board_hand_suit}\nHand Ranking: {self.getStrength()}')
      print()