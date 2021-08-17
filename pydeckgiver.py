import random

suits = '♠ ♡ ♢ ♣'.split();
numbers = '2 3 4 5 6 7 8 9 10 J Q K A'.split();

def create_deck(aleatory: bool = True) -> list:
    deck: list = [(a, b) for a in suits for b in numbers]
    if aleatory:
        random.shuffle(deck)
    return deck

def to_distribute(deck: list, participants: int = 4) -> tuple:
    result: list = []
    for x in range(0, participants):
        data: dict = deck[x::participants]
        result.append(data)
    return tuple(result)


if __name__ == '__main__':

    # Input how many participants and checks if its pair.
    participants: int = int(input('How many participants? Must be int and pair number: '))
    if participants % 2 == 1:
        print(f'Participants must be a pair number! Try again.\nPress enter to exit...')
        input(); quit()

    # Create a deck and distribute.
    deck: list = create_deck(aleatory=True)
    deck: tuple = to_distribute(deck=deck, participants=participants)

    # Create player numbers.
    players: list = [f'P{x}' for x in range(1, participants + 1)]

    # Create hand for each participant.
    hand: dict = {p:d for p, d in zip(players, deck)}

    # Join cards and print final result.
    for p, d in hand.items():
        cards = ' '.join(f'{a}{b}' for a, b in d)
        print(f'{p}: {cards}')
    print(f'Press enter to exit!')
    input()