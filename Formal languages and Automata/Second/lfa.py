from states import Producoes

glci  = [["S -> Tb | a | bT | D | E"], ["T -> a"], ["C -> c | f | D"], ["D -> d"], ["E -> $"]]
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

def update(prod, op):
  if op == 1:
    for i in range(0, nvar):
      if nvar[i].name == prod.name:
        nvar[i] = prod
  elif op == 2:
    for i in range(0, vari):
      if vari[i].name == prod.name:
        vari[i] = prod

def canFindNVar(name):
  for i in nvar:
    if i.name == name:
      return True
  return False


def findNVar(name):
   for i in nvar:
      if i.name == name:
	 return i
   return False


def canFindVar(name):
  for i in vari:
    if i.name == name:
      return True
  return False


def findVar(name):
   for i in vari:
      if i.name == name:
	 return i
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
    if j.islower() == True and canFindVar(j)  == False:
      new = Producoes(j, [], [j], [])
      vari.append(new)
      prod.append(new)


def createNewFirstProduct (glc):
  # S ->
  for i in glc:
    createFirst(i)

  for i in glc:
    createUpper(i)

  for i in glc:
    createLower(i)
  
  for i in nvar:
     getFirst(i)


def getAsList(rules):
   x = []
   y = []

   for i in range(0, len(rules)):
      if rules[i] == "|" :
	 x.append(i)
   
   #if "|" in rules:
   x.append(len(rules))

   i = 0
   for j in x:
      y.append(rules[i:j])
      i = j + 1
   
   return y


def clearSpaceList(aux):
   lists = []
   for i in aux:
      lists.append(i.replace(" ", ""))
   return lists   


def getFirst(prod):
  print(prod.name + " => ")
  lists = clearSpaceList(getAsList(prod.rules))
  first = []

  for i in lists:
     if i not in first:
        first.append(i[0])	  
  
  print("FIRST:  %s" % first)
 

if __name__ == '__main__':
  main()

  print("-------------VARIAVEIS---------------")
  for i in vari:
    print(i.name)
  
  print("-------------NAO TERMINAIS-----------")
  for j in nvar:
      print(j.name)
