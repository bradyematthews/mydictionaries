# This program uses a dictionary as a deck of cards.
import random
def main():
    # Create a deck of cards.
    card_deck = create_deck() #Call the first function. "Card_Deck" becomes the dictionary because it receives the dictionary that is returned from the "return" function.

    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))



    # Deal the cards.
    deal_cards(card_deck,num_cards)

    
    

# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck(): # This function is a value-returning function
    # Create a dictionary with each card and its value. Name of the card is the Key, the number of the card is the Value. --> The name of the card is unique, therefore that makes a good key because a key needs to be unique. These are numbers we need to use to get the sum total, they can't be the key because the key has to be a string.
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck # This returns something whenever it executes



# The deal_cards function deals a specified number of cards
# from the deck.

def deal_cards(deck, number): # This function is a void function. Expecting two arguments: a dictionary and expecting the number of cards the user wants to deal
    # Initialize an accumulator for the hand value.
    hand_value = 0
    
    
    # DATA VALIDATION
    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck (52).
    if number > len(deck):
        number = len(deck) # Max number they can pick is 52
    
    

    # Deal the cards and accumulate their values.
    for card in range(number): # in range(number) because "number" represents the number of cards the user wants (Ex. number 5 --> we would want the for look to go 5 times)
       #popitem() option: card, value = deck.popitem() --> This wouldn't work efficiently for this because we want it to be random
        card = random.choice(list(deck))
        print(card) #popitem() always produces the last arguments (Ex. 5, it produced the last 5 values in the deck)
        value = deck[card]
        hand_value += value


    

    # Display the value of the hand.
    print(hand_value) # Once the For loop is done, we print the hand_value
    
    

# Call the main function.
main()
