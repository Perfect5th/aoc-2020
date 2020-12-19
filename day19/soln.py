import re

from utils import memoize, input_groups


def parse_rule(rule, rules_dict):
    num, rule = rule.split(': ')

    rule = rule.replace('"', '')

    if '|' in rule:
        rule = rule.split(' | ')
        rule = [r.split(' ') for r in rule]
        rule = (rule[0], rule[1])
    elif len(rule) > 1:
        rule = rule.split(' ')

    rules_dict[int(num)] = rule


def solve1(ipt):
    rules, messages = input_groups(ipt)

    rules_dict = {}
    for rule in rules:
        parse_rule(rule, rules_dict)

    @memoize
    def build(num):
        rule = rules_dict[num]

        if type(rule) == str:
            return rule

        if type(rule) == tuple:
            lhs, rhs = rule
            lhs = ''.join(map(lambda r: build(int(r)), lhs))
            rhs = ''.join(map(lambda r: build(int(r)), rhs))
            return f'(({lhs})|({rhs}))'

        if type(rule) == list:
            built = ''.join(map(lambda r: build(int(r)), rule))
            return f'({built})'

    built = f'^{build(0)}$'

    print(len(list(filter(lambda m: re.match(built, m), messages))))


def solve2(ipt):
    rules, messages = input_groups(ipt)

    rules_dict = {}
    for rule in rules:
        parse_rule(rule, rules_dict)

    @memoize
    def build(num, depth=0):
        rule = rules_dict[num]

        if num == 8:
            return f'{build(42)}+'

        if num == 11 and depth < 10:
            return f'({build(42)}({build(11, depth+1)})?{build(31)})'
        elif num == 11:
            return f'({build(42)}{build(31)})'

        if type(rule) == str:
            return rule

        if type(rule) == tuple:
            lhs, rhs = rule
            lhs = ''.join(map(lambda r: build(int(r)), lhs))
            rhs = ''.join(map(lambda r: build(int(r)), rhs))
            return f'(({lhs})|({rhs}))'

        if type(rule) == list:
            built = ''.join(map(lambda r: build(int(r)), rule))
            return f'({built})'

    built = f'^{build(0)}$'

    print(len(list(filter(lambda m: re.match(built, m), messages))))
