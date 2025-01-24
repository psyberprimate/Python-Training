from card import Card
from seat import Seat
from user import User

def text_user_interface():
    """Pleb tier interface - sorry
    """ 
    # a dummy seat for accessing the class
    dummy_seat = Seat(seat_id="0") 
    while(True):
        print("****Cinema ticket booking****")
        customer_name = input("Please enter your name: ")
        print("Please select your preferred seat: ")
        print(dummy_seat.get_seats())
        customer_seat_choice = input("Your seat choice: ")
        customer_card_type = input("Your payment card type: ")
        customer_card_number = input("Your payment card number: ")
        customer_card_cvc = input("Your payment card cvc: ")
        customer_card_name = input("Card holder name: ")
        
        try:
            seat = Seat(seat_id=customer_seat_choice)
        except Exception as e:
            print(e)
            print("Error - re-enter values")
            continue
        try:
            card = Card(type=customer_card_type,
                                number=int(customer_card_number),
                                cvc=int(customer_card_cvc),
                                holder=customer_card_name)
        except Exception as e:
            print(e)
            print("Error - re-enter values")
            continue
        
        user = User(name=customer_name)
        user.buy(seat=seat, card=card)

def main():
    text_user_interface()

if __name__ == "__main__":
    print("Cinema ticket booking")
    main()