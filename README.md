# Card-Game

This program was created through the following assumptions:
          The computer is the dealer and the player is the user.  Overview of the game:  
                    First the program selects hands of two cards each, one for the dealer and one for the player  
                    Next it is the player's Turn While his/her hand is valued at under 21, he/she has the option of getting an additional card. However, any time that the player's hand is valued at 22 or more the game ends and the player loses.  
                    Next it is the dealer's Turn While the dealer's cards are worth 16 or less, the dealer draws a card  
                    The dealer's hand and the player's hand are compared and a winner is determined  
          Scoring  
                    If one of the following is true, the dealer wins  
                              The dealer has Black Jack (to be defined) or  
                              The player's hand > 21  
                    Elif one of the following is true, the player wins  
                              The player has Black Jack  
                              The dealer's hand > 21  
                              The player's hand > the dealer's hand
                          Else the dealer wins  
                     Some Assumptions  
                               Suits (Clubs, Diamonds, Hearts, Spades) will be ignored  
                               We will assume that there are only 13 different cards: ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
                               There can never be more than 4 of the same card type in play at any time, e.g., if there are 4 10s in play, and a fifth ten is randomly selected, a new card must be drawn in its place
                               'A' can be worth either 1 or 11 points  2-10 are worth their face value (2 is worth 2, 3 is worth 3, etc.)
                               'J','Q' and 'K' are each worth 10 points  
                               Black Jack is a hand consisting of 2 cards: an 'A' and a card worth 10 points  
