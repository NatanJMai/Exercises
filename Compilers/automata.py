import string

class state (object):
  def createState(self, name):
    self.name  = name
    self.rules = []


def openFileAndReturnList():
  f  = open("def.fd", 'r')
  pr = str(f.readline().strip(' \t\n\r'))
  sy = str(f.readline().strip(' \t\n\r'))
  iD = str(f.readline().strip(' \t\n\r'))
  return (f, pr, sy, iD)


def returnAlph(entry, remove):
  alphabet = []
  for i in entry:
    if i not in alphabet and i not in remove:
      alphabet.append(i)
  return alphabet


def main():
  trp = openFileAndReturnList()
  fle = trp[0]
  pr  = trp[1][4:]
  iD  = trp[2][4:]
  remove   = [',', ' ']
  alphabet = returnAlph(pr + iD + string.ascii_lowercase, remove) 
  for i in alphabet:
    print(" %s " % i)



if __name__ == "__main__":
  main()
