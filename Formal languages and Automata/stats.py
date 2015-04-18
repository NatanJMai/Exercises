class States(object):
    def __init__ (self, name, rules, start, final):
        self.name      = name
        self.rules     = rules
        self.beginner  = start
        self.final     = final
