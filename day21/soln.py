def solve1(ipt, print_result=True, **kwargs):
    food_set = set()
    allergen_set = set()
    food_list = []

    for line in ipt:
        foods, allergens = line.split(' (')
        foods = foods.split(' ')
        allergens = allergens[9:].rstrip(')').split(', ')
        food_list.append((foods, allergens))

        for f in foods:
            food_set.add(f)

        for a in allergens:
            allergen_set.add(a)

    result = set()
    for a_s in allergen_set:
        foods = set(food_set)

        for i, a in food_list:
            if a_s in set(a):
                foods &= set(i)

        result |= foods
    
    others = food_set - result

    total = 0
    for f, _ in food_list:
        total += len([0 for fs in f if fs in others])

    if print_result:
        print(total)

    return food_set - others, allergen_set, food_list


def solve2(ipt, **kwargs):
    bad_food, allergen_set, food_list = solve1(ipt, False)

    allergen_food_dict = {a: set(bad_food) for a in allergen_set}
    
    for fs, a_s in food_list:
        for a in a_s:
            allergen_food_dict[a] &= set(fs)

    while any([len(fs) > 1 for fs in allergen_food_dict.values()]):
        for a_s, fs in allergen_food_dict.items():
            if len(fs) == 1:
                allergen_food_dict = {k: v-fs if k != a_s else fs for k, v in allergen_food_dict.items()}

    print(','.join(map(lambda k: list(k[1])[0], sorted(allergen_food_dict.items()))))