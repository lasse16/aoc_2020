CARD_PUB = 8987316
DOOR_PUB = 14681524
SUBJECT_NUMBER = 7
DIVISOR = 20201227


def main():
    card_loop = 1
    while transform_subject_number(card_loop) != CARD_PUB:
        card_loop += 1

    value = transform_subject_number(card_loop, DOOR_PUB)

    print(f"Secret key card [{value}]")


def transform_subject_number(exponent, subject_number=SUBJECT_NUMBER):
    return pow(subject_number, exponent, DIVISOR)


if __name__ == "__main__":
    main()
