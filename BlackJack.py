import random
import os

class Dealer:
    card_pool = ['A', 'J', 'Q', 'K'] + range(2,11)
    card_pool = card_pool * 4
    random.shuffle(card_pool)
    
    def __init__(self, dealer_hand = [], dCount = []):
        self.dealer_hand = dealer_hand
        self.dCount = dCount

    def hit(self, hand, count):
        self.hand = hand
        self.count = count
        
        drawed_card = Dealer.card_pool.pop()
        self.hand.append(drawed_card)
        self.count.append(drawed_card)
        for i in self.count:
            if i == 'J' or i == 'Q' or i == 'K':
                self.count.remove(i)
                self.count.append(10)
            elif i == 'A':
                self.count.remove(i)
                if sum(self.count) < 11:
                    self.count.append(11)
                else:
                    self.count.append(1)
        
        return self.hand, self.count
    
    def stay(self):
        print "You stayed!"
        
    def dealerHit(self, hand, count):
        self.hand = hand
        self.count = count
        if sum(self.count) < 17:
            Dealer.hit(self, hand, count)
        
        
    def endGame(self):
        print 'Thank you for playing.'
    
class Player(Dealer):    
    
    def __init__(self, money = 100, player_hand = [], pCount = []):
        self.money = money
        self.player_hand = player_hand
        self.pCount = pCount
    
    def bet(self, amount = None):
        self.amount = amount
        self.amount = float(raw_input('Enter your bet: '))
        while True: 
            if self.amount <= self.money:
                return self.amount
                break
            else:
                self.amount = float(raw_input('Your limit exceed. Bet again: '))
                return self.amount
    
    def winMoney(self):
        self.money = self.money + (self.amount * 2)
        return self.money
    
    def loseMoney(self):
        self.money = self.money - self.amount
        return self.money


def manager():
    dealer = Dealer()
    player = Player()
        
    set_money = str(raw_input("Set your own game money? Default is $100. Y/N: ")).upper()
    while True:
        if set_money == 'Y':
            player.money = float(raw_input('Enter the amount: '))
            break
        elif set_money == 'N':
            player.money = float(player.money)
            break
        else:
            set_money = str(raw_input("Y or N only: ")).upper()
            

    ##################
    while True:
        num = 1
        while num <= 2:
            dealer.hit(dealer.dealer_hand, dealer.dCount)
            player.hit(player.player_hand, player.pCount) 
            num += 1
        print "\nDealer's hand: {}\nPlayer's hand: {}".format(dealer.dealer_hand, player.player_hand)
        print "Dealer's count: {}\nPlayer's count: {}".format(sum(dealer.dCount), sum(player.pCount))
        player.bet()
        
        while player.money > 0:
            dealer.dealerHit(dealer.dealer_hand, dealer.dCount)
            hit = str(raw_input('Hit? Y/N: ')).upper()
            if hit == 'Y':
                player.hit(player.player_hand, player.pCount)
                print "\nDealer's hand: {}\nPlayer's hand: {}".format(dealer.dealer_hand, player.player_hand)
                print "Dealer's count: {}\nPlayer's count: {}".format(sum(dealer.dCount), sum(player.pCount))
                if sum(player.pCount) <= 21:
                    if sum(player.pCount) > sum(dealer.dCount) or sum(dealer.dCount) > 21:
                        player.winMoney()
                        print 'Player won!'
                        print 'Balance: ${}'.format(player.money)
                        break
                    elif sum(player.pCount) < sum(dealer.dCount) and 20 <= sum(player.pCount) < 21:
                        player.loseMoney()
                        print 'Player lost!'
                        print 'Balance: ${}'.format(player.money)
                        break
                    elif sum(player.pCount) == sum(dealer.dCount):
                        print 'Tie!'
                        print 'Balance: ${}'.format(player.money)
                        break
                    else:
                        continue
                else:
                    player.loseMoney()
                    print 'Player lost!'
                    print 'Balance: ${}'.format(player.money)
                    break
                
            elif hit == 'N':
                player.stay()
                print "\nDealer's hand: {}\nPlayer's hand: {}".format(dealer.dealer_hand, player.player_hand)
                print "Dealer's count: {}\nPlayer's count: {}".format(sum(dealer.dCount), sum(player.pCount))
                if sum(player.pCount) <= 21:
                    if (sum(player.pCount) > sum(dealer.dCount) and sum(dealer.dCount) >= 17) or sum(dealer.dCount) > 21:
                        player.winMoney()
                        print 'Player won!'
                        print 'Balance: ${}'.format(player.money)
                        break
                    elif sum(player.pCount) < sum(dealer.dCount):
                        player.loseMoney()
                        print 'Player lost!'
                        print 'Balance: ${}'.format(player.money)
                        break
                    else:
                        print 'Tie!'
                        print 'Balance: ${}'.format(player.money)
                        break
                else:
                    player.loseMoney()
                    print 'Player lost!'
                    print 'Balance: ${}'.format(player.money)
                    break
            else:
                print "Y or N only."
        
        if player.money > 0:
            con = str(raw_input('Again? Y/N: ')).upper()
            if con == 'Y':
                dealer.dealer_hand = []
                dealer.dCount = []
                player.player_hand = []
                player.pCount = []
            elif con == 'N':
                player.endGame()
                break
            else:
                con = str(raw_input('Y or N only.\nAgain? Y/N: '))
        elif player.money <= 0:
            player.endGame()
            break



print "Welcome to play the Black Jack!"

while True:
    manager()
    con = str(raw_input('New Game? Y/N: ')).upper()
    if con == 'Y':
        pass
    elif con == 'N':
        break        

