def main():
    input = "input.txt"
    foods = parse_input_into_foods(input)
    all_ingredients = []
    all_allergenes_and_possible_ingredients = {}
    for food in foods:
        ingredients, allergenes = food
        all_ingredients.extend(ingredients)
        for allergene in allergenes:
            possible_ingredients = all_allergenes_and_possible_ingredients.get(
                allergene, False
            )
            contained_ingredients = set(ingredients)
            if possible_ingredients:
                all_allergenes_and_possible_ingredients[
                    allergene
                ] = possible_ingredients.intersection(contained_ingredients)
            else:
                all_allergenes_and_possible_ingredients[
                    allergene
                ] = contained_ingredients
    allergic_ingredients = set(
        ingredient
        for allergene in all_allergenes_and_possible_ingredients.values()
        for ingredient in allergene
    )
    non_allergic_ingredients = [
        ingredient
        for ingredient in all_ingredients
        if ingredient not in allergic_ingredients
    ]
    print(len(non_allergic_ingredients))


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
