from states import Producoes

glci  = [["S -> aSFGb | a | b"], ["T -> b | cd"]]
prod  = []
nvar  = []
vari  = []

def main():
  createNewFirstProduct(glci)

def createFirst(i):
  name = i[0][0]
  rule = i[0][4:].strip()
  new  = Producoes(name, rule, [], [])
  prod.append(new)
  nvar.append(new)

def canFindNVar(name):
  for i in nvar:
    if i.name == name:
      return True
  return False

def canFindVar(name):
  for i in vari:
    if i.name == name:
      return True
  return False

def createUpper(i):
  rule = i[0][4:].strip()
  for j in rule:
    if j.isupper() == True and canFindNVar(j) == False:
      new = Producoes(j, [], [], [])
      nvar.append(new)
      prod.append(new)


def createLower(i):
  rule = i[0][4:].strip()
  for j in rule:
    if j.islower() == True and canFindVar(j) == False:
      new = Producoes(j, [], [j], [])
      vari.append(new)
      prod.append(new)

def createNewFirstProduct (glc):
  for i in glc:
    createFirst(i)
    createUpper(i)
    createLower(i)

if __name__ == '__main__':
  main()
  for i in nvar:
    print(i.name)

  for i in vari:
    print(i.name)
