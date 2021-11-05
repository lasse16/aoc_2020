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
    canonical = {}
    while all_allergenes_and_possible_ingredients:
        known = [
            (k, list(v)[0])
            for k, v in all_allergenes_and_possible_ingredients.items()
            if len(v) == 1
        ]
        for k, v in known:
            canonical[k] = v
            del all_allergenes_and_possible_ingredients[k]
            for a in all_allergenes_and_possible_ingredients:
                if v in all_allergenes_and_possible_ingredients[a]:
                    all_allergenes_and_possible_ingredients[a].remove(v)
    dangerous_list = ",".join([v for k, v in sorted(canonical.items())])
    print(dangerous_list)


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
