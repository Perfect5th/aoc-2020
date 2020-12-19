from utils import input_groups


def build_rules_dict(rules):
    # rules_dict is label: (range(), range())
    rules_dict = {}
    for rule in rules:
        label, ranges = rule.split(': ')
        lrange, rrange = ranges.split(' or ')
        llow, lhigh = [int(i) for i in lrange.split('-')]
        rlow, rhigh = [int(i) for i in rrange.split('-')]

        rules_dict[label] = (range(llow, lhigh+1), range(rlow, rhigh+1))

    return rules_dict


def solve1(ipt, print_result=True, **kwargs):
    rules, _, tickets = input_groups(ipt)
    rules_dict = build_rules_dict(rules)

    def is_val_invalid(val):
        return all([not (val in ranges[0] or val in ranges[1]) for _, ranges in rules_dict.items()])

    def add_invalids(ticket):
        return sum(filter(is_val_invalid, [int(i) for i in ticket.split(',')]))

    if print_result:
        print(sum(map(add_invalids, tickets[1:])))

    return filter(lambda t: add_invalids(t) == 0, tickets[1:])


def solve2(ipt, **kwargs):
    rules, your_ticket, _ = input_groups(ipt)
    your_ticket = [int(i) for i in your_ticket[1].split(',')]
    valid_tickets = solve1(ipt, False, **kwargs)
    valid_tickets = [[int(i) for i in t.split(',')] for t in valid_tickets]
    rules_dict = build_rules_dict(rules)
    candidates = {k: set() for k, _ in rules_dict.items()}

    def valid_for_rule(v, rule):
        range1, range2 = rules_dict[rule]
        return v in range1 or v in range2

    for rule in candidates.keys():
        for i in range(len(your_ticket)):
            if all([valid_for_rule(t[i], rule) for t in valid_tickets]):
                candidates[rule].add(i)

    while any([len(vals) > 1 for vals in candidates.values()]):
        for rule, vals in candidates.items():
            if len(vals) == 1:
                candidates = {r: v-vals if r != rule else vals for r, v in candidates.items()}

    if 'is_test' in kwargs:
        print(candidates)
    else:
        total = 1
        for val in [your_ticket[list(v)[0]] for r, v in candidates.items() if 'departure' in r]:
            total *= val

        print(total)
