played_decks = []


def main():
    input = "input.txt"
    deck_player1, deck_player2 = parse_input_into_decks(input)

    while deck_player1 and deck_player2:
        deck_player1, deck_player2 = play_one_round(deck_player1, deck_player2)
    score = calculate_score(deck_player1, deck_player2)
    print(score)


def play_one_round(deck1, deck2):
    if round_already_played(deck1, deck2):
        return deck1, []
    played_decks.append((deck1, deck2))

    player1_card = deck1.pop(0)
    player2_card = deck2.pop(0)

    if player1_card >= len(deck1) and player2_card >= len(deck2):
        player1_won = recursive_combat((player1_card, deck1), (player2_card, deck2))
    else:
        player1_won = player1_card > player2_card

    if player1_won:
        deck1.append(player1_card)
        deck1.append(player2_card)
    else:
        deck2.append(player2_card)
        deck2.append(player1_card)

    return deck1, deck2


def recursive_combat(player1, player2):
    pass


def round_already_played(deck1, deck2):
    return (deck1, deck2) in played_decks


def calculate_score(deck1, deck2):
    for deck in [deck for deck in [deck1, deck2] if deck]:
        score = 0
        for index, card in enumerate(deck[::-1], 1):
            score += index * card
        return score


def parse_input_into_decks(input):
    with open(input) as file:
        deck_1, deck_2 = file.read().split("\n\n")

        cards_1 = deck_1.splitlines(keepends=False)[1:]
        cards_2 = deck_2.splitlines(keepends=False)[1:]

        return parse_cards_to_deck(cards_1), parse_cards_to_deck(cards_2)


def parse_cards_to_deck(cards):
    return [int(card) for card in cards]


if __name__ == "__main__":
    main()
