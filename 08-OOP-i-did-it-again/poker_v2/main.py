from hand import Hand


def main() -> None:
    player_1 = Hand(input("Enter Player 1's cards: "))
    player_2 = Hand(input("Enter Player 2's cards: "))

    if player_1 > player_2:
        print('Player 1 wins!')
        print(f'A {player_1.poker_hand} beats A {player_2.poker_hand}')
    else:
        print('Player 2 wins!')
        print(f'A {player_2.poker_hand} beats A {player_1.poker_hand}')


if __name__ == '__main__':
    main()