class Producoes(object):
   def __init__ (self, name, rules, first, follow):
      self.name      = name
      self.rules     = rules
      self.first     = first
      self.follow    = follow

   def setRules(self, rules):
      self.rules = rules

   def setName(self, name):
      self.name = name
