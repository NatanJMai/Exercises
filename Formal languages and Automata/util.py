#!/usr/bin/env python
# -*- coding: utf-8 -*-

from states import States
import unittest

alphbt  = ['a', 'b', 'c']                            # alphabet

q0       = States('q0'   , [['a', 'q1']       , ['b', 'q2'], ['c', '']]         , True , False )
q1       = States('q1'   , [['a', '']         , ['b', 'q0'], ['c', 'q3']]       , False, False )
q2       = States('q2'   , [['a', 'q3']       , ['b', 'q4'], ['c', '']]         , False, False )
q3       = States('q3'   , [['a', '']         , ['b', '']  , ['c', 'q4']]       , False, False )
q4       = States('q4'   , [['a', 'q3']       , ['b', '']  , ['c', 'q5']]       , False, False )
q5       = States('q5'   , [['a', '']         , ['b', '']  , ['c', '']]         , False, True )

statsK   = [q0, q1, q2, q3, q4, q5]

#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Get the type according the definition.
#------------------------------------------------------------
def getTypeAF():
    for stat in statsK:
        for rul in stat.rules:
            if len(rul) > 2:
                return True
    return False


#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 05/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Verify if all states are created
#------------------------------------------------------------
def verifyAllStates():
    for stat in statsK:
        for rul in stat.rules:
            for name in range(1, len(rul)):
                if rul[name] != "":
                    if findStateWithName(rul[name]) == "":
                        return False
    return True


#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 05/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Verify if all lyrics are created
#------------------------------------------------------------
def verifyAllLetters():
    for stat in statsK:
        for rul in stat.rules:
            if rul[0] != "":
                if not rul[0] in alphbt:
                    return False
    return True


#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 05/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Accept or Reject messages.
#------------------------------------------------------------
def acceptReject(variable):
    if variable == True:
        print("ACCEPT!")
        return True

    else:
        print("REJECT!")
        return False


#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Verify if is an AFND or AFD
#------------------------------------------------------------
def init():
    print("(1) Testar AFD\n(2) Testar AFND\n(3) Transformar AFND em AFD\n(4) Rodar testes")

    opt = int(raw_input("> "))

    if not verifyAllStates():
        print("ERROR - 001")
        return False

    if not verifyAllLetters():
        print("ERROR - 002")
        return False

    if opt != 4:
        entry = raw_input("Entrada: ")
        if entry == "" or verifyAllEntries(entry) == False:
            print("ERROR - 003")
            return False

    if opt == 1:
        if getTypeAF() == True:
            print("A maquina é como AFD!")
            return False

        return acceptReject(testAFD(entry, statsK))

    elif opt == 2:
        if getTypeAF() != True:
            print("A maquina é como AFND!")
            return False

        return acceptReject(testAFD(entry, testAFND(statsK)))

    elif opt == 3:
        if getTypeAF() != True:
            print("A maquina é como AFND!")
            return False

        spp = testAFND(statsK)

        for stt in spp:
            print("----------------------")
            print(stt.name)
            for rul in stt.rules:
                print("%s" % rul)

    elif opt == 4:
        tests()

#-------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Verify if all letters are in the entry
#-------------------------------------------------------------
def verifyAllEntries(entry):
    for ent in entry:
        if not ent in alphbt:
            return False


#-------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Find a state with a word
#-------------------------------------------------------------
def findStateWithName(name):
    for state in statsK:
        if state.name == name:
            return state

    return ""


#-------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Return the next state according a word
#-------------------------------------------------------------
def returnNextState(word, state):
    for rul in range(0, len(state.rules)):
        if word in state.rules[rul]:
            return (findStateWithName(state.rules[rul][1]))

    return ""


#-------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: All the others tests to AFD
#-------------------------------------------------------------
def testAFD(word, statsK):
    if verifyAllEntries(word) == False:
        print("The alphabet is wrong!")
        return False

    stateNow = statsK[0]

    for wrd in word:
        stateNow = returnNextState(wrd, stateNow)

        if stateNow == "":
            return False

        if stateNow.final == True:
            return True

    if stateNow.final == False:
        return False



#-------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Here start the tests to AFND
#-------------------------------------------------------------



#-------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Return all possibles states of a state according
#          a letter
#-------------------------------------------------------------
def returnStatesWhenALetter(name, letter):
    state = findStateWithName(name)
    retur = []

    if state == "":
        return

    for rul in state.rules:
        if rul[0] == letter:
            for ii in range(1, len(rul)):
                retur.append(rul[ii])
    return retur


#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Concatenate the name of new state.
#------------------------------------------------------------
def concName(word):
    strg = ""

    for ind in range(1, len(word)):
        strg = strg + word[ind]

    if findStateWithName(strg) == "":
        return strg
    else:
        return ""


#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Rules to create a new state
#------------------------------------------------------------
def createNewState(word, name, final):
    newStateName = concName(word)
    lastState    = word[len(word) - 1]

    if newStateName == "":
        return ""

    final = findStateWithName(lastState).final

    if findStateWithName(newStateName) == "":
        newState     = States(newStateName, "", False, final)
        statsK.append(newState)
        return word[1:]


#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Update the rules of state.
#------------------------------------------------------------
def updateRule(stateName):
    name        = ""
    fullList    = []
    lists       = []

    for lett in stateName:
        name = name + lett

    state = findStateWithName(name)

    if state == "":
        return

    for alp in alphbt:
        states = []
        lists  = [alp]
        for name in stateName:
            states.append(returnStatesWhenALetter(name, alp))

        for stt in states:
            for jj in stt:
                if jj != "" and jj not in lists:
                    lists.append(jj)

        fullList.append(lists)
    state.setRules(fullList)


#-------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Concatenate a list.
#-------------------------------------------------------------
def concList(listA):
    newStr = ""

    for lst in listA:
        newStr = newStr + lst

    return newStr


#-------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: The state will be deleted?
#-------------------------------------------------------------
def isDeleted(stateName):
    for state in statsK:
        for rul in state.rules:
            if concList(rul[1:]) == stateName and state.name != stateName:
                return True
    return False


#-------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Verify all the states, if it will be deleted and
#          it isn't one start then remove it
#-------------------------------------------------------------
def verifyUtils():
    for stt in statsK:
        if not isDeleted(stt.name) and stt.start == False:
            statsK.remove(stt)
            verifyUtils()


#-------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: All others tests to AFND
#-------------------------------------------------------------
def testAFND(statsK):
    for state in statsK:
        for rul in state.rules:
            if len(rul) > 2:
                name = createNewState(rul, state.name, state.final)
                if name != "":
                    updateRule(name)

    verifyUtils()

    for state in statsK:
        full = []
        for rul in state.rules:
            li = [rul[0]]
            li.append(concList(rul[1:]))
            full.append(li)

        state.setRules(full)

    return statsK


#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 06/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Definitions of tests to run.
#------------------------------------------------------------
class MyTest(unittest.TestCase):

    def test(self):
        entry = 'bbc'
        if getTypeAF() == True:
            self.assertEqual(acceptReject(testAFD(entry, testAFND(statsK))), True)
        else:
            self.assertEqual(acceptReject(testAFD(entry, statsK)), True)

    def test2(self):
        entry = 'accc'
        if getTypeAF() == True:
            self.assertEqual(acceptReject(testAFD(entry, testAFND(statsK))), True)
        else:
            self.assertEqual(acceptReject(testAFD(entry, statsK)), True)

    def test3(self):
        entry = 'bacc'
        if getTypeAF() == True:
            self.assertEqual(acceptReject(testAFD(entry, testAFND(statsK))), True)
        else:
            self.assertEqual(acceptReject(testAFD(entry, statsK)), True)

    def test4(self):
        entry = 'bbacc'
        if getTypeAF() == True:
            self.assertEqual(acceptReject(testAFD(entry, testAFND(statsK))), True)
        else:
            self.assertEqual(acceptReject(testAFD(entry, statsK)), True)

    def test5(self):
        entry = 'bbbaca'
        if getTypeAF() == True:
            self.assertEqual(acceptReject(testAFD(entry, testAFND(statsK))), False)
        else:
            self.assertEqual(acceptReject(testAFD(entry, statsK)), False)

    def test6(self):
        entry = 'abbacb'
        if getTypeAF() == True:
            self.assertEqual(acceptReject(testAFD(entry, testAFND(statsK))), False)
        else:
            self.assertEqual(acceptReject(testAFD(entry, statsK)), False)

    def test7(self):
        entry = 'c'
        if getTypeAF() == True:
            self.assertEqual(acceptReject(testAFD(entry, testAFND(statsK))), False)
        else:
            self.assertEqual(acceptReject(testAFD(entry, statsK)), False)

    def test8(self):
        entry = 'bacacc'
        if getTypeAF() == True:
            self.assertEqual(acceptReject(testAFD(entry, testAFND(statsK))), True)
        else:
            self.assertEqual(acceptReject(testAFD(entry, statsK)), True)

#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 06/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Running tests
#------------------------------------------------------------
def tests():
    unittest.main()

