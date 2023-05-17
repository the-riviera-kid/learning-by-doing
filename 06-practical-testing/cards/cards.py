from pure_cards import parse_card

def main():
    user_input = input('What is your card? ')
    card_description = parse_card(user_input)
    print(card_description)

if __name__ == '__main__':
    main()