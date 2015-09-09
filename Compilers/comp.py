import string
import automaton as AUT
from enum     import Enum

class Token(object):
  def init(self, typ, name, desc):
    self.typ  = typ
    self.name = name
    self.desc = desc

class Type(Enum):
  ID  = 0
  KEY = 1
  SYM = 2
  ERR = 3

automaton = AUT.autMain()

keywords = ["file", "find", "each", "directory", "new", "print", "tar", "zip", "where", "canfind", "name", "return", "path", "author", "delete","and", "or"]
sy       = ["=","!",">"," <", "->",":","(",")",'"'] 
ID       = []

separ = ['-', '>', '(', '"', '=', '!', '"', '>', '<', ':'] 
sepNT = [' ', '\n', '\t']

for i in string.ascii_lowercase:
  ID.append(i)


def createToken(name, desc):
  token = Token()
  if name == "ERROR":
    typ = Type.ERR
  elif desc in keywords:
    typ = Type.KEY
  elif desc in sy:
    typ = Type.SYM
  else:
    typ = Type.ID
  token.init(typ, name, desc)
  return token

def run(stt):
  i      = 0
  j      = 0
  final  = len(stt) - 1 
  atual  = automaton.states[0]
  wrd    = ""
  don    = False
  tokens = []
  while(i < final):
    wrd  = ''

    while (don != True and j < final):
      let  = stt[j]
      if not let in sepNT:
        nextS = AUT.nextState(atual, let)
        if nextS == ():
          tokens.append(createToken("ERROR", let))
        elif nextS != ():
          atual = nextS
          wrd   = wrd + let
          don   = atual.final
          if don == True:
            tokens.append(createToken(atual.name, wrd))
      j += 1
    
    i    = j  
    don  = False


  '''
  while(i < final):
    let  = stt[i]
    wrd  = wrd + let
    last = atual
    print(let)

    if let in separ:
      nextS = AUT.nextState(atual, let)
      atual = nextS
      if not don:
        tokens.append(createToken(last.name,  wrd[:len(wrd) - 1]))
        don = True

      wrd = let
      tokens.append(createToken(atual.name, wrd))
      wrd = ''
      i   += 1
    
    elif let in sepNT:
      tokens.append(createToken(last.name, wrd[:len(wrd) - 1]))
      wrd = ''
      i += 1

    else:
      nextS = AUT.nextState(atual, let)
      atual = nextS
      #print(atual.name)
      i += 1
  '''  
  for i in tokens:
    print(i.name, i.typ, i.desc)

def main():
  file_input = open("tests.fd", 'r')
  
  for i in file_input:    
    run(i)


if __name__ == "__main__":
  main()
