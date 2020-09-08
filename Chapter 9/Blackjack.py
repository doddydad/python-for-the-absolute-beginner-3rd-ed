# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:19:55 2020

@author: Andrew
"""


#Blackjack
#From 1 to 7 players compete against a dealer

import cards, games

class BJ_Cards(cards.Card):
    """ A blackjack card. """
    ACE_VALUE = 1
    
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Cards.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v
    
class BJ_Deck(cards.Deck):
    """ A Blackjack deck. """
    def populate(self):
        for suit in BJ_Cards.SUITS:
            for rank in BJ_Cards.RANKS:
                self.cards.append(BJ_Cards(rank, suit))
                
class BJ_Hand(cards.Hand):
    """ A blackjack Hand. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name =  name
        
    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    
    @property
    def total(self):
        # if a card in the hand has value None, then total is None
        for card in self.cards:
            if not card.value:
                return None
            
        #add all values, treat ace as 1
        t = 0
        for card in self.cards:
            t += card.value
            
        #determine if hand contains an ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Cards.ACE_VALUE:
                contains_ace = True
                
        #I love you honey
        #if player == "Beth" or "Andrew":
        #    contains_ace = True
        
        #If hand contains ace and total low enough, treat ace as 11
        if contains_ace and t <= 11:
            t += 10
            
        return t
    
    def is_busted(self):
        return self.total > 21
    
class BJ_Player(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + 
                                    ", do you want to hit? (y/n): ")
        return response == "y"
    
    def bust(self):
        print(self.name, "busts.")
        self.lose()
        
    def lose(self):
        print(self.name, "loses.")
    
    def win(self):
        print(self.name, "wins.")
        
    def push(self):
        print(self.name, "pushes.")
        
class BJ_Dealer(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17
    
    def bust(self):
        print(self.name, "busts.")
        
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
        
class BJ_Game(object):
    """ A Blackjack Game. """
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
            
        self.dealer = BJ_Dealer("Dealer")
        
        self.deck = BJ_Deck()
        
    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp
    
    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
                
    def play(self):
        #new deck each round
        self.deck.populate()
        self.deck.shuffle()
        # deal 2 cards to everyone to start
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        #hide first dealer's card
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)
        
        # Deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)
            
        self.dealer.flip_first_card()
        
        if not self.still_playing:
            #since all players busted, just show dealers hand
            print(self.dealer)
        else:
            #deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)
            
            if self.dealer.is_busted():
                #everyone still playing wins
                for player in self.still_playing:
                    player.win()
        
            else:
                #compare each player remaining to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        
        #remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()
        
        
def main():
    print("\t\tWelcome to Blackjack!\n")
    
    names = []
    number = games.ask_number("How many players? (1-7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
        
    print()
    game = BJ_Game(names)
    
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you wanna play again? (y/n): ")
        
main()