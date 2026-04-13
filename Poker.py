import random
class Card:
    
    def __init__(self, value, suite):
        self.value = value 
        self.suite = suite
    def __repr__(self):
        return "{} of {}".format(self.value,self.suite)

class Deck:
   
    def __init__(self):
        suites = ["S","D","H","C"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        
        self.cards = [Card(value,suite) for suite in suites for value in values]
        #print (f"printing self.cards: {self.cards}")

    def __repr__(self):
        return f"{self.count()} Cards left in the deck"
    
    def __iter__(self):
        return iter(self.cards)
    
    def count(self):
        return len(self.cards)
    
    def _deal(self,num):
        count = self.count()
        actual = min([count,num])
        if count == 0:raise ValueError("All cards have been dealt with")
        if num > 52:raise ValueError("you cannot deal with more than 52 cards..")
            
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        print (f"{cards} have been dealt with")
        print (f"printing cards: {cards}")
        return cards
    
    def deal_card(self,dealt_cards):
        print (f"these are dealt_cards: {dealt_cards}")
        self.dealt_cards=dealt_cards
        #print (f"printing self._deal(1): {self._deal(1)}")
        #print (f"printing self._deal(1)[0]: {self._deal(1)[0]}")
        return random.choice(self.dealt_cards)
    
    def deal_hand(self,hand_size):
        print(f"this is self._deal(hand_size): {self._deal(hand_size)}")
        return self._deal(hand_size)
    
    def shuffle(self):
      
        if self.count()< 52: raise ValueError("only full deck can be shuffled..")
        random.shuffle(self.cards)
        return self.cards

#c = Card("A","H")
#print (c)

d = Deck()

print ("....................printing the deck...................")
print (f"display using __repr__ dunder method: {d}")
print ("")
shuffled_cards = d.shuffle()
print ("....................shuffled cards now...............")

print (f"Shuffled Cards in the Deck of {d.count()} cards:{shuffled_cards}")
#print ("..................cards have been shuffled..........")
print ("")

print (f"display using __repr__ dunder method: {d}")
print ("")

print ("------------------deal method to pick cards------------------")
print (d._deal(5))
dealt_cards = d._deal(5)
print (f"display using __repr__ dunder method: {d}")
print ("")

print ("------------------dealing a single card------------------")
print (d.deal_card(dealt_cards))
dealt_hand = d.deal_hand(5)
print (f"dealt_hand: {dealt_hand}")


print ("-------------------iterating through the deck-------------------")
for card in d:
    print (card)
