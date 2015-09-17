import string
import automaton as AUT
from enum     import Enum

class Token(object):
  def init(self, typ, name, desc, line, column):
    self.typ    = typ
    self.name   = name
    self.desc   = desc
    self.line   = line
    self.column = column

class Type(Enum):
  ID  = 0
  KEY = 1
  SYM = 2
  ERR = 3

automaton = AUT.autMain()

keywords = ["file", "find", "each", "directory", "new", "print", "tar", "zip", "where", "canfind", "name", "return", "path", "author", "delete","and", "or"]
sy       = ["=","!",">"," <", "->",":","(",")",'"'] 

sepNT = [' ', '\n', '\t']


def createToken(name, desc, line, column):
  token = Token()
  if name == "ERROR":
    typ = Type.ERR
  elif desc in keywords:
    typ = Type.KEY
  elif desc in sy:
    typ = Type.SYM
  else:
    typ = Type.ID
  token.init(typ, name, desc, line, column)
  return token

def run(stt, column):
  i      = 0
  j      = 0
  final  = len(stt) - 1 
  atual  = automaton.states[0]
  wrd    = ""
  don    = False
  tokens = []
  tok   = createToken("$", "$", 0, 0)

  while(i < final):
    wrd  = ''

    while (don != True and j < final):
      let  = stt[j]
      if not let in sepNT:
        nextS = AUT.nextState(atual, let)
        if nextS == ():
          tokens.append(createToken("ERROR", let, column, j + 2))
        elif nextS != ():
          atual = nextS
          wrd   = wrd + let
          don   = atual.final
          if don == True:
            tokens.append(createToken(atual.name, wrd, column, j + 2))
      j += 1
    
    i    = j  
    don  = False
  
  return tokens

def main():
  x = 0
  tokens     = []
  tok        = createToken("$", "$", 0, 0)
  file_input = open("tests.fd", 'r')
  
  for i in file_input:    
    x += 1
    tokens += run(i, x)
  
  tokens.append(tok)

  for i in tokens:
    #print(i.name,i.desc, i.line, i.column)
    print("%s & %s & %d & %d \\\\" %(i.name, i.desc, i.line, i.column))


if __name__ == "__main__":
  main()
