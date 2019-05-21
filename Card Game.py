import random
deck=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck_status = [4]*13

dealer=[]
player=[]

dealers_value = 0
players_value = 0
black_jack = ('J' or 'Q' or 'K' or 10) and 'A'

def black_jack_victory(list):
    return ('10' in list or 'J' in list or 'Q' in list or 'K' in list) and ('A' in list)

def sum_hand(list):
    sum = 0
    a = 0
    for i in list:
        if i == 'J':
            sum += 10
        elif i == 'Q':
            sum += 10
        elif i == 'K':
            sum += 10
        elif i == 'A':
            a += 1
        else:
            sum += int(i)
    if sum <= 10 and a == 1:
        sum += 11
    if sum <= 10 and a > 1:
        sum += a
    if sum > 10:
        sum += a
    return sum    

def give_card():

    #pick a random card
    index = random.randint(0,len(deck)-1)   
    while deck_status[index] <= 0:
        index = random.randint(0,len(deck)-1)
    card = deck[index]
    deck_status[index] -= 1
    return card

def player_turn():
        answer=True
        while answer==True:
            response=input('Would you like an additional card? ')
            if response=='yes':
                player.append(give_card())
                print('Dealer: ',dealer)
                print('Player: ',player)
                if sum_hand(player) > 21:
                    answer=False
            elif response=='no':
                dealer_turn()
                print('Dealer: ',dealer)
                print('Player: ',player)
                answer=False
            else:
                print('Not a valid answer')

def dealer_turn():
    while sum_hand(dealer)<=16:
        dealer.append(give_card())

def game():
    player.append(give_card())
    player.append(give_card())
    dealer.append(give_card())
    dealer.append(give_card())
    print('Dealer: ',dealer)
    print('Player: ',player)
    if black_jack_victory(dealer):
        print('You Lose because the dealer has Black Jack')
    elif black_jack_victory(player):
        print('You Win because you have Black Jack')
    else:
        player_turn()
        dealer_turn()
        if sum_hand(player)>21:
            print('You Lose because your hand is worth more than 21')
        elif sum_hand(dealer)>21:
            print("You Win because the dealer's hand is worth more than 21")
        elif sum_hand(player)>sum_hand(dealer):
            print('You Win because you have more cards than the dealer')
        else:
            print('You Lose because rules')
game()
