from states import Producoes

glci  = [["S -> Tb | a | xT | Co | Ep |Eo | E"], ["T -> o"], ["C -> w "], ["D -> i"], ["E -> $ | e | T"], ["F -> f"], ["G -> gig | S"]]
#glci  = [["A -> B | C | D | a"], ["B -> b"], ["C -> c"], ["D -> d"]]
#glci  = [["X -> YZ | aY | bY | z | c"], ["Y -> a"], ["Z -> $"]]
prod  = []
nvar  = []
vari  = []

def main():
  for i in glci:
    print(i)

  createNewFirstProduct(glci)
  firstOfNVar()
  adjust()
  #for i in nvar:
    #print(i.name)
    #print(i.first)
  for i in range(0, len(nvar)):
#    print("NOME => %s" % nvar[i].name)
    nvar[i].follow = startFollow(getIndexNVar(nvar[i].name))

  for i in nvar:
    print("---------------------------------------------------------------------------------")
    print("NOME: ===========> %s" % i.name)
    print("FIRST ===========> %s" % i.first)
    print("FOLLW ===========> %s" % i.follow)
  
def whoCalledMe(name):
  lists = []
  for i in range(0, len(nvar)):
    prodList = clearSpaceList(getAsList(nvar[i].rules))
    for j in prodList:
      if name in j:
        lists.append(nvar[i].name)
  return lists


def findFollow(i, called):
  #i eh o indice dochamado
  #ind eh o indice dos chamadores
  #S -> T
  #chamador = S
  #chamado  = T
  lists = ["%"]
  for cal in called:
    ind     = getIndexNVar(cal)
    rulInd  = clearSpaceList(getAsList(nvar[ind].rules))
    for indRul in rulInd:
      for indIndRul in range(0, len(indRul)):
        if indRul[indIndRul] == nvar[i].name:
          if (indIndRul + 1) < len(indRul):                   #aqui eh o caso 1
            if indRul[indIndRul + 1].isupper():
              newName = getIndexNVar(indRul[indIndRul + 1])
              first   = nvar[newName].first
            else:
              newName = getIndexVar(indRul[indIndRul + 1])
              first   = vari[newName].first
            if "%" in lists: lists.remove("%")
            for firs in first:
              if firs not in lists:
                lists.append(firs)
          else:
#            print(indRul[indIndRul])
            foll = startFollow(ind)
            if "%" in foll: foll.remove("%")
            for firs in foll:
              if firs not in lists:
                lists.append(firs)
  return lists

  


def startFollow(i):
  called = whoCalledMe(nvar[i].name)
  return(findFollow(i, called))








#   FIRST FIRST FIRST FIRST
# Tem $ 
def adjust():
  alls = []
  for i in range(0, len(nvar)): 
    first = []
    for j in range(0, len(nvar[i].first)):
      if "@" in nvar[i].first[j]:
        index = nvar[i].first[j].index('@')
        if (index + 1) < len(nvar[i].first[j]):
          proxi = index + 1
          nomeP = nvar[i].first[j][proxi]
          indV  = getIndexProd(nomeP)
          for xp in prod[indV].first: 
            if xp not in first:
              first.append(xp)
        else:
          if "$" not in first:
            first.append("$")
      else:
        b = nvar[i].first[j][0]
        if b not in first and not b.isupper():
          first.append(b)
    nvar[i].first = first




def firstOfNVar():
  for i in range(0, len(nvar)):
    fixFirst(nvar[i])
  
  for j in range(0, len(nvar)): 
    first = []
    for i in range(0, len(nvar[j].first)):
      if nvar[j].first[i].isupper():
        a = nvar[j].first[i]
        nvar[j].first[i] = ""        
      else:
        first.append(nvar[j].first[i])
    nvar[j].first = first


def returnUpperLetters(conj):
  x = []
  for i in conj:
    if i[0].isupper():
      x.append(i[0])
  return x

def fixFirst(prod):
  x = returnUpperLetters(prod.first) 
  b = getIndexNVar(prod.name)
  
  for up in range(0, len(x)):
    a = getIndexNVar(x[up])
    fixFirst(nvar[a])
    for i in nvar[a].first:
      if i == "$":
        for p in range(0, len(nvar[b].first)):
          if nvar[a].name in nvar[b].first[p]:
            nvar[b].first[p] = nvar[b].first[p].replace(nvar[a].name, "@")

      elif i not in nvar[b].first:
        nvar[b].first.append(i)


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


def getIndexNVar(name):
  for i in range(0, len(nvar)):
    if nvar[i].name == name:
      return i
  return -1


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


def getIndexVar(name):
  for i in range(0, len(vari)):
    if vari[i].name == name:
      return i
  return -1


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

###

def getIndexProd(name):
  for i in range(0, len(prod)):
    if prod[i].name == name:
      return i
  return -1


def canFindProd(name):
  for i in prod:
    if i.name == name:
      return True
  return False


def findProd(name):
   for i in prod:
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

# Principal funcao
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


def containsUpperLetter(conj):
  for i in conj:
    if i.isupper():
      return True
  return False


def getFirst(prod):
#  print(prod.name + " => ")
  lists = clearSpaceList(getAsList(prod.rules))
  first = []
  for i in lists:
     if i not in first:
       if containsUpperLetter(i):
         first.append(i)
       else:
        first.append(i[0])	  
  
  j = getIndexNVar(prod.name)
  
  if j != -1: nvar[j].first = first

#  print("FIRST:  %s" % first)
 

if __name__ == '__main__':
  main()

