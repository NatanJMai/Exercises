class States(object):
    def __init__ (self, name, rules, start, final):
        self.name      = name
        self.rules     = rules
        self.start     = start
        self.final     = final

    def setRules(self, rules):
        self.rules = rules

    def setName(self, name):
        self.name = name

    def setFinal(self, final):
        self.final = final
