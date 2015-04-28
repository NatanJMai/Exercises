#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stats import States

#q0 = States('q0', (('a', 'q0'), ('b', 'q1'), ('c', 'q2')), True, False ) # q0 Definition
#q1 = States('q1', (('a', 'q1'), ('b', 'q0'), ('c', 'q0')), False, False ) # q1 Definition
#q2 = States('q2', (('a', 'q0'), ('b', 'q0'), ('c', 'q0')), False, True) # q2 Definition
#statsK = (q0, q1, q2)

statsK  = ('S', 'a', 'b', 'aa', 'bb', 'fim')    # Set of states
alphbt  = ('a', 'b')                            # alphabet

S       = States('S'    , (('a', 'b', 'fim')   , ('b', 'b'))   , True , False )
a       = States('a'    , (('a', 'fim') , ('b', 'b'))   , False, False )
b       = States('b'    , (('a', 'c', 'a')   , ('b', 'fim')) , False, False )
fim     = States('fim'  , (('1', '3') , ('2', '3')) , False, True  )

statsK  = [S, a, b, fim]


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
    # First verification - Verify if all letters are in alphabet  #
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

#                                                                                 #
#                                  AFND                                           #
#                                                                                 #

def returnAllStates(state):
    stt = findStateWithName(state)

    if stt == "":
        return

    #print("Sta: %s" % state)
    #print(len(stt.rules))
    #print(len(stt.rules[0]))

    for j in range(0, len(stt.rules)):
       for i in range(1, len(stt.rules[j])):
           print("Estado %s, regras => %s" % (state, stt.rules[j][i]))

    #return (.rules)

def concName(word):
    strg = ""

    for j in range(1, len(word)):
        strg = strg + word[j]

    if findStateWithName(strg) == "":
        return strg


def concState(word):
    for j in range(1, len(word)):
        #print(word[j])
        returnAllStates(word[j])




def createNewState(word):
    concName(word)
    concState(word)

def testAFND(word, statsK):
    # First verification - Verify if all letters are in alphabet  #
    if verifyAllEntries(word) == False:
        print("The alphabet is wrong!")
        return



    for jj in statsK:
        for ii in jj.rules:
            if len(ii) > 2:
                print("Name: %s" % jj.name)
                createNewState(ii)

