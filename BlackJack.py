from random import shuffle
suit=('Hearts','Diamond','Spades','Club')
rank=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
   
common_deck=Deck()  
common_deck.shuffle()

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return f"{self.rank} {self.suit}"
    
    
class Deck:
    def __init__(self):
        self.all_cards=[]
        for i in suit:
            for j in rank:
                new_card=Card(i,j)
                self.all_cards.append(new_card)
    def shuffle(self):
        return shuffle(self.all_cards)
    def deal_card(self):
        if not self.all_cards==[]:
            return self.all_cards.pop(0)
        else:
            pass
    
def deal_1():
    return str(common_deck.deal_card())


class Player:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.player_cards=[deal_1(),deal_1()]
    def __str__(self):
        return f"Player name: {self.name} \nBalance: {self.balance}\n"
    def bet(self,bet_value):
        self.bet_value=bet_value
        if self.balance>=bet_value:
            self.balance-=bet_value
            return True
        else:
            print("Bet a lower amount.")
            return False
    def show(self):
        return self.player_cards
    def hit(self):
        self.player_cards.append(deal_1())
        return self.show()
    def empty(self):
        common_deck.all_cards.extend(self.player_cards)
        self.player_cards=[deal_1(),deal_1()]
    

class Dealer:
    def __init__(self):
        self.dealer_cards=[deal_1(),deal_1()]
        self.balance=0
    def show(self):
        return self.dealer_cards
    def hit(self):
        self.dealer_cards.append(deal_1())
        return self.show()
    def __str__(self):
        return f"Dealer Balance: {self.balance}\n"
    def empty(self):
        common_deck.all_cards.extend(self.dealer_cards)
        self.dealer_cards=[deal_1(),deal_1()]

def find_sum(card_arr,P_or_D):
    l,val=[],0
    for c in card_arr:
        l=list(map(str,c.split()))
        if l[0]=='Ace' and P_or_D=='P':
            ace_val=int(input("\nYou got an Ace:which value you want?\tEnter 1 or 11:\tYou chose:"))
            val+=ace_val
        else:
            val+=Card(l[1],l[0]).value
    return val
        
class Driver():
    player1=Player('Mrun',2000)
    print(player1)
    
    dealer=Dealer()
    print(dealer)

    
    choice =True
    while choice:
        common_deck.shuffle()
        won_flag=' '
        jackblack=[False,False]
        #### PLAYER TURN #####

        player_current=player1.show()
        print(f"Player Cards: {player_current}")
        card_sum_p=find_sum(player_current,'P')
        print(f"Player Cards: {player_current}\tPlayer Total: {card_sum_p}")

        dealer_current=dealer.show()
        print(f"Dealer Cards : [ {dealer_current[0]} , ' HIDDEN ' ]\tDealer's Card value: {values[dealer_current[0].split()[0]]}")

        confirm_bet=False
        while not confirm_bet:
            bet_val=int(input(f"\nHow much do you want to bet?\tBid must be less than {player1.balance}\nYou bid:"))
            confirm_bet=player1.bet(bet_val)
        print(f"You have {player1.balance} chips left.\tBet placed ! Let's play !")

        while card_sum_p<21:
            choice=input("\nDo you want to hit?\t'Y' or 'N'\tYou chose:")
            if choice.upper()=='Y':
                hit_seq=player1.hit()
                print(f"\nPlayer got: {hit_seq}")
                card_sum_p=find_sum(hit_seq,'P')
                print(f"Player got: {hit_seq}\tPlayer Card Sum : {card_sum_p}")
                if card_sum_p==21:
                    print("\nPlayer got BLACK-JACK!!")
                    jackblack[0]=True
                    break
                elif card_sum_p>21:
                    won_flag='D'
                    break
            else:
                break
        print(f"PLAYER'S FINAL CARD SUM :{card_sum_p}\n")
        if not won_flag =='D':
            #### DEALER TURN #####

            print("Dealer's Turn !")
            card_sum_d=find_sum(dealer_current,'D')
            print(f"Dealer Cards:{dealer_current}\tDealer Total: {card_sum_d}")
            if card_sum_d<17 and not card_sum_d>=21:
                while card_sum_d<17 and not card_sum_d>=21:
                    print("Dealer : Card sum is less than 17.")
                    hit_seq=dealer.hit()
                    card_sum_d=find_sum(hit_seq,'D')
                    print(f"Dealer got: {hit_seq}\tDealer Card Sum : {card_sum_d}")
            if card_sum_d==21:
                print("Dealer got BLACK-JACK!")
                jackblack[1]=True
            elif card_sum_d>21:
                won_flag='P'


            print(f"DEALER'S FINAL CARD SUM ::{card_sum_d}\n")
        if won_flag == ' ' and True not in jackblack:
            if card_sum_d>card_sum_p:
                won_flag='D'
            elif card_sum_d<card_sum_p:
                won_flag='P'
            elif card_sum_d==card_sum_p:
                print("It's a Push. No one won.")
                player1.balance+=player1.bet_value
        if won_flag=='D' or jackblack==[False,True]:
            print("Dealer Won")
            dealer.balance+=player1.bet_value
        elif won_flag=='P'or jackblack==[True,False]:
            player1.balance+=2*(player1.bet_value)
            print("Player Won")
        elif jackblack==[True,True]:
            print("Both got Black-Jack.Its a Tie")
            player1.balance+=player1.bet_value
        print(f"Player's Balance: {player1.balance}\tDealer's Balance: {dealer.balance}\n*******************************************************************")
        
        Y_N=input("Want to continue playing?\t You chose:")
        if Y_N.upper()=='Y':
            choice = True
            player1.empty()
            dealer.empty()
        elif Y_N.upper()=='N':
            choice = False
