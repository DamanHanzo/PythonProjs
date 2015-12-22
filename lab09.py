
import cards

import random
#random.seed( 25 )

# Create the deck of cards
def play_war(h1, h2):
    #loop until one hand is empty
    while (len(h1)!=0 and len(h2)!=0):
        h1,h2 = play_one(h1,h2)
        print("hand1:",h1)
        print("hand2:",h2)
        if input("Keep Going: (Nn) to stop:").lower() == 'n':
            break
    if len(h1)>len(h2):
        print('Player 1 Wins')
    elif len(h2) > len(h1):
        print('Player 2 Wins')
    else:
        print('Tie')


def play_one(h1, h2):
    player1_card = h1.pop( 0 )
    player2_card = h2.pop( 0 ) 

    val1=player1_card.get_rank()
    if val1==1:
        val1=13
        
    val2=player2_card.get_rank()
    if val2==1:
        val2=13
    
    # get the value of top1: val1
    # get the value of top2: val2

    if val1 > val2:
        # h1 gets both cards
        h1.append(player1_card)
        h1.append(player2_card)
    elif val2 > val1:
        h2.append(player1_card)
        h2.append(player2_card)
    else:
        # insert the poped card back
        h1.append(player1_card)
        h2.append(player2_card)
        
        

        
    return h1,h2

def main():
    my_deck = cards.Deck()

    player1_list = []
    player2_list = []

    my_deck.shuffle()

    while not my_deck.is_empty():
        player1_list.append( my_deck.deal() )
        player2_list.append( my_deck.deal() )

    player1_list = player1_list[:5]
    player2_list = player2_list[:5]
    play_war(player1_list, player2_list)


if __name__ == "__main__":
    main()

