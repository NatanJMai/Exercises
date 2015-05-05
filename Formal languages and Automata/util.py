#!/usr/bin/env python
# -*- coding: utf-8 -*-

from states import States

alphbt  = ['a', 'b', 'c']                            # alphabet

q0       = States('q0'   , [['a', 'q1']       , ['b', 'q2'], ['c', '']]         , True , False )
q1       = States('q1'   , [['a', '']         , ['b', 'q0'], ['c', 'q3']]       , False, False )
q2       = States('q2'   , [['a', 'q3']       , ['b', 'q4'], ['c', '']]         , False, False )
q3       = States('q3'   , [['a', '']         , ['b', '']  , ['c', 'q4']]       , False, False )
q4       = States('q4'   , [['a', 'q3']       , ['b', '']  , ['c', 'q5']]       , False, False )
q5       = States('q5'   , [['a', '']         , ['b', '']  , ['c', '']]         , False, True )

statsK  = [q0, q1, q2, q3, q4, q5]

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
#   DATE : 01/05/2015
#   FILE : util.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Verify if is an AFND or AFD
#------------------------------------------------------------
def init():

    if not verifyAllStates():
        print("ERROR - 001")
        return

    if not verifyAllLetters():
        print("ERROR - 002")
        return

    entry = raw_input("Entry: ")

    if entry == "":
        print("ERROR - 003")
        return

    if getTypeAF():
        testAFD(entry, testAFND(entry, statsK))
    else:
        testAFD(entry, statsK)


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
        return

    stateNow = statsK[0]

    for wrd in word:
        stateNow = returnNextState(wrd, stateNow)

        if stateNow == "":
            print("FINAL - REJEITO")
            return

        print("     w-> %s, state -> %s" %(wrd, stateNow.name))
        if stateNow.final == True:
            print("FINAL - ACEITO")
            return

    if stateNow.final == False:
        print("FINAL - REJEITO")
        return



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
def testAFND(word, statsK):
    if verifyAllEntries(word) == False:
        print("The alphabet is wrong!")
        return

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
