# Reference -> https://gist.github.com/danoneata/16bfcb01154ce1081e00

class Expr(object):
    def accept(self, visitor):
        method_name = 'visit_{}'.format(self.__class__.__name__.lower())
        visit = getattr(visitor, method_name)
        return visit(self)


class Int(Expr):
    def __init__(self, value):
        self.value = value


class Add(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Mul(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Visitor(object):
    pass


class Eval(Visitor):
    def visit_int(self, i):
        return i.value

    def visit_add(self, a):
        return a.left.accept(self) + a.right.accept(self)

    def visit_mul(self, a):
        return a.left.accept(self) * a.right.accept(self)


class Print(Visitor):
    def visit_int(self, i):
        return i.value

    def visit_add(self, a):
        return '({} + {})'.format(a.left.accept(self), a.right.accept(self))

    def visit_mul(self, a):
        return '({} * {})'.format(a.left.accept(self), a.right.accept(self))


if __name__ == '__main__':
    expr = Add(Add(Int(1), Int(2)), Mul(Int(2), Add(Int(3), Int(3))))
    print(expr.accept(Print()))
    print(expr.accept(Eval()))
