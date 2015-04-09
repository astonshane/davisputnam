class Literal:
    def __init__(self, name, negated):
        self.name = name
        self.negated = negated

    def __str__(self):
        if(self.negated):
            return "~" + self.name
        else:
            return self.name

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if other == None:
            return False
        else:
            return self.name == other.name and self.negated ==  other.negated

    def __ne__(self, other):
        return not self.__eq__(other)
