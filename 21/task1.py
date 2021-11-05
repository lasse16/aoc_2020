def main():
    input = "input.txt"
    foods = parse_input_into_foods(input)
    print(foods)


def parse_input_into_foods(input):
    foods = []
    with open(input) as file:
        for line in file:
            ingredients, allergenes = line.split("(")
            allergenes = allergenes[len("contains") :].strip()
            allergenes = allergenes[:-1]
            allergenes = [allergene.strip() for allergene in allergenes.split(",")]
            ingredients = ingredients.strip()
            ingredients = [ingredient.strip() for ingredient in ingredients.split()]
            foods.append((ingredients, allergenes))
    return foods


if __name__ == "__main__":
    main()
