#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stats import States

#q0 = States('q0', (('a', 'q0'), ('b', 'q1'), ('c', 'q2')), True, False ) # q0 Definition
#q1 = States('q1', (('a', 'q1'), ('b', 'q0'), ('c', 'q0')), False, False ) # q1 Definition
#q2 = States('q2', (('a', 'q0'), ('b', 'q0'), ('c', 'q0')), False, True) # q2 Definition
#statsK = (q0, q1, q2)

alphbt  = ['a', 'b']                            # alphabet

q0      = States('q0'   , [['a', 'q0', 'q1']       , ['b', 'q0', 'q2']]  , True , False )
q1      = States('q1'   , [['a', 'qf']             , ['b', '']]          , False, False )
q2      = States('q2'   , [['a', '' ]              , ['b', 'qf']]        , False, False )
qf      = States('qf'   , [['a', 'qf']             , ['b', 'qf']]        , False, True  )

statsK  = [q0, q1, q2, qf]

def verifyAllEntries(entry):
    for j in entry:
        if not j in alphbt:
            return False

def findStateWithName(name):
    for state in statsK:
        if state.name == name:
            return state

    return ""

def returnNextState(word, state):
    for ind in range(0, len(state.rules)):
        if word in state.rules[ind]:
            return (findStateWithName(state.rules[ind][1]))

    return ""

def testAFD(word, statsK):
    if verifyAllEntries(word) == False:
        print("The alphabet is wrong!")
        return

    stateNow = statsK[0]

    for w in word:
        stateNow = returnNextState(w, stateNow)
        print("     w-> %s, state -> %s" %(w, stateNow.name))
        if stateNow.final == True:
            print("FINAL - ACEITO")
            return

    if stateNow.final == False:
        print("FINAL - REJEITO")
        return


##     AFND     ##
##              ##


def returnStatesWhenALetter(name, letter):
    state = findStateWithName(name)
    retur = []

    if state == "":
        return

    for jj in state.rules:
        if jj[0] == letter:
            for ii in range(1, len(jj)):
                retur.append(jj[ii])
    return retur


def concName(word):
    strg = ""

    for j in range(1, len(word)):
        strg = strg + word[j]

    if findStateWithName(strg) == "":
        return strg
    else:
        return ""

# Create a new state and return its states like a tuple
def createNewState(word, name, final):
    newStateName = concName(word)

    if newStateName == "":
        return ""

    final = findStateWithName(newStateName[len(newStateName) - 2:]).final

    if findStateWithName(newStateName) == "":
        newState     = States(newStateName, "", False, final)
        statsK.append(newState)
        return word[1:]

def updateRule(stateName):
    name        = ""
    fullList    = []
    lists       = []

    for ii in stateName:
        name = name + ii

    state = findStateWithName(name)

    if state == "":
        return

    for alp in alphbt:
        states = []
        lists  = [alp]
        for nn in stateName:
            states.append(returnStatesWhenALetter(nn, alp))

        for ss in states:
            for jj in ss:
                if jj != "" and jj not in lists:
                    lists.append(jj)

        fullList.append(lists)
    state.setRules(fullList)

def concList(listA):
    newStr = ""

    for jj in listA:
        newStr = newStr + jj

    return newStr

def isDeleted(stateName):
    for jj in statsK:
        for rul in jj.rules:
            if concList(rul[1:]) == stateName and jj.name != stateName:
                return True
    return False

def verifyUtils():
    for stt in statsK:
        if not isDeleted(stt.name) and stt.start == False:
            statsK.remove(stt)
            verifyUtils()


def testAFND(word, statsK):
    if verifyAllEntries(word) == False:
        print("The alphabet is wrong!")
        return

    for jj in statsK:
        for ii in jj.rules:
            if len(ii) > 2:
                name = createNewState(ii, jj.name, jj.final)
                if name != "":
                    updateRule(name)

    verifyUtils()

    for jj in statsK:
        full = []
        for rl in jj.rules:
            li = [rl[0]]
            li.append(concList(rl[1:]))
            full.append(li)

        jj.setRules(full)

    return statsK

    #Just print
'''    for spp in statsK:
        print("\n----------------------\n")
        print(spp.name)
        print(spp.rules) '''
