def create_graphmap(ipt):
    graphmap = {}

    for i in ipt:
        tokens = i.split(' ')
        parent = ' '.join(tokens[:2])
        children = []

        if not 'no other bags' in i:
            for i in range(4, len(tokens), 4):
                children.append((int(tokens[i]), ' '.join(tokens[i+1:i+3])))

        graphmap[parent] = children

    return graphmap


def part1(ipt, target):
    graphmap = create_graphmap(ipt)

    def search_graph(root):
        for c in graphmap[root]:
            if target in c[1] or search_graph(c[1]):
                return 1

        return 0

    return sum([search_graph(k) for k, _ in graphmap.items()])


def part2(ipt, target):
    graphmap = create_graphmap(ipt)

    def search_graph(root):
        total = 0
        for c in graphmap[root]:
            total += c[0] + c[0] * search_graph(c[1])

        return total

    return search_graph(target)


if __name__ == '__main__':
    with open('input.txt') as fp:
        ipt = [l for l in fp]
        print(part1(ipt, 'shiny gold'))
        print(part2(ipt, 'shiny gold'))
