import re


OPS = {
    '+': lambda lhs, rhs: lhs + rhs,
    '*': lambda lhs, rhs: lhs * rhs,
}


class Lisper:
    def __init__(self, expr, part_2=False):
        self.expr = expr
        self.i = 0
        self.part_2 = part_2

    def parse_primary(self):
        if re.match(r'^\d$', self.expr[self.i]):
            self.i += 1
            return int(self.expr[self.i-1])

        if self.expr[self.i] == '(':
            self.i += 1
            internal = self.parse_expr()
            self.i += 1
            return internal

    def parse_plus(self):
        lhs = self.parse_primary()

        while self.i < len(self.expr) and self.expr[self.i] == '+':
            self.i += 1
            op = self.expr[self.i-1]
            rhs = self.parse_primary()
            lhs = (op, lhs, rhs)

        return lhs

    def parse_expr(self):
        lhs = self.parse_plus() if self.part_2 else self.parse_primary()
        target = '*' if self.part_2 else '+*'

        while self.i < len(self.expr) and self.expr[self.i] in target:
            self.i += 1
            op = self.expr[self.i-1]
            rhs = self.parse_plus() if self.part_2 else self.parse_primary()
            lhs = (op, lhs, rhs)

        return lhs


def interp_expr(expr):
    if type(expr) == int:
        return expr

    if type(expr) == tuple:
        return OPS[expr[0]](interp_expr(expr[1]), interp_expr(expr[2]))


def solve(ipt):
    print(sum([interp_expr(Lisper(expr.replace(' ', '')).parse_expr()) for expr in ipt]))
    print(sum([interp_expr(Lisper(expr.replace(' ', ''), True).parse_expr()) for expr in ipt]))


with open('input.txt') as fp:
    ipt = [l.rstrip('\n') for l in fp]
    solve(ipt)