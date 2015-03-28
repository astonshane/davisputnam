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
