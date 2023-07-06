import random
import tkinter


def load_images(card_images : list) -> None:

    """_summary_
    Load the images from cards directory to a list with tuples for each card e.g value and image of card
    Raises:
        ValueError: _description_
    """    

    suits=['heart', 'club','diamond','spade']
    face_cards = ['jack', 'queen', 'king']
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        raise ValueError(f"tkVersion is not 8.6 -> tkversion is: {tkinter.TkVersion}")   
    # For each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = 'Section9 - Modules and Functions/cards/{}_{}.{}'.format(str(card), suit, extension) #Section9 - Modules and Functions/ Section9 - Modules and Functions\cards\1_club.png
            print(name)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))
        #next face cards
        for card in face_cards:
            name = f'Section9 - Modules and Functions/cards/{str(card)}_{suit}.{extension}'
            print(name)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def _deal_card(frame : tkinter.Frame) -> tuple:

    #pop the next card off the top of the deck
    next_card = deck.pop(0)
    #add the image to a Label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    #now return the card's face value
    return next_card

def score_hand(hand : list)->int:
    #Calculate the toal score of all cards in the list.
    #Only one ace can have the value 11, and this will be reduced to 1 if then would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        #if bust then check if there is an ace and substract 10
        if score > 21 and ace:
            score -= 10
            ace = False    
    #print(score)         
    return score

def deal_dealer()->None:
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    #print(f"Dealer score {dealer_score}")
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21:
        result_text.set("Player Wins!")
    elif dealer_score > player_score and len(player_hand) == len(dealer_hand):
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw!")    

def deal_player()->None:
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    # global player_score
    # global player_ace
    # card_value = deal_cards(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     card_value = 11
    #     player_ace = True
    # player_score += card_value    
    # #if we would bust, check if there is an ace and substract
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")
    #     player_score = 0
    # print(locals())


def new_game()->None:
    global dealer_hand, player_hand, dealer_card_frame, player_card_frame, result_text, deck

    dealer_hand = []
    player_hand = []
    result_text.set("")

    dealer_card_frame.destroy()
    dealer_card_frame.forget()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=(2))

    player_card_frame.destroy()
    player_card_frame.forget()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row="2", column="1", columnspan=3, sticky="w")

    #Check if the deck is low on cards and re-shuffle the deck
    if len(deck) > 10:
        pass
        #print(len(deck))
    else:
        shuffle()

    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    player_score_label.set(score_hand(dealer_hand))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def shuffle()->None:
    #Create the list to store the dealer's and player's hands
    global deck, dealer_hand, player_hand
    deck = []
    deck = list(cards)
    random.shuffle(deck)


def play()->None:
    new_game()
    mainWindow.mainloop()
    

#Set up the screen and frames for the dealer and player
mainWindow = tkinter.Tk() 
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column = 0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# #embedded frame hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=(2))

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
#Embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row="2", column="1", columnspan=3, sticky="w")

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=3)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=4)

quit_button = tkinter.Button(button_frame, text="Quit", command=mainWindow.destroy)
quit_button.grid(row=0, column=5)
#load cards
cards = []
load_images(cards)
shuffle()
new_game()
if __name__ == "__main__":

    #Set up screen and frames for the dealer and the player
    play()