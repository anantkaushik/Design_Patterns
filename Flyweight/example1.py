class User:
    """
    Unoptimized implementation
    """
    def __init__(self, name):
        self.name = name


class User2:
    """
    Optimized implementation as one name is stored only once
    """
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings)-1
        self.names = [get_or_add(x) for x in full_name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])


if __name__ == '__main__':
    u2 = User2('Jim Jones')
    u3 = User2('Frank Jones')
    print(u2)
    print(u3)
    print(User2.strings)

