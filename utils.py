from functools import lru_cache


def input_groups(ipt):
    # splits input on blank lines
    groups = []

    curr_group = []
    for l in ipt:
        if l == '':
            groups.append(curr_group)
            curr_group = []
            continue

        curr_group.append(l)

    groups.append(curr_group)

    return groups


def memoize(func):
    @lru_cache(maxsize=None)
    def call(*args, **kwargs):
        return func(*args, **kwargs)

    return call