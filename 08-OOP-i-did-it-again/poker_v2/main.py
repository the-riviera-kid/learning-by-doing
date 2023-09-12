from hand import Hand


def main() -> None:
    player_1 = Hand(input("Enter Player 1's cards: "))
    player_2 = Hand(input("Enter Player 2's cards: "))

    if player_1 > player_2:
        print('Player 1 wins!')
        print(f'A {player_1} beats A {player_2}')
    elif player_2 > player_1:
        print('Player 2 wins!')
        print(f'A {player_2} beats A {player_1}')
    else:
        print('Draw')


if __name__ == '__main__':
    main()