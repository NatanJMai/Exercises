#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stats import States

#q0 = States('q0', (('a', 'q0'), ('b', 'q1'), ('c', 'q2')), True, False ) # q0 Definition
#q1 = States('q1', (('a', 'q1'), ('b', 'q0'), ('c', 'q0')), False, False ) # q1 Definition
#q2 = States('q2', (('a', 'q0'), ('b', 'q0'), ('c', 'q0')), False, True) # q2 Definition
#statsK = (q0, q1, q2)

statsK  = ('q0', 'q1', 'q2', 'qf')    # Set of states
alphbt  = ('a', 'b')                            # alphabet

q0      = States('q0'   , (('a', 'q0', 'q1') , ('b', 'q0'))    , True , False )
q1      = States('q1'   , (('a', 'q2', 'q2')       , ('b', ''))      , False, False )
q2      = States('q2'   , (('a', 'qf', 'q1', 'q2')       , ('b', ''))      , False, False )
qf      = States('qf'   , (('a', '')         , ('b', ''))      , False, True  )

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

def returnAllStates(state, letter):
    stt   = findStateWithName(state)
    newst = ""

    if stt == "":
        return

    #print("Sta: %s" % state)
    #print("Lett: %s" % letter)

    for ii in range(0, len(stt.rules)):
        for jj in range(0, len(stt.rules[ii]) - 1):
            if stt.rules[ii][0] == letter:
                newst = newst + stt.rules[ii][jj + 1]
                print("Teste: %s" % str(stt.rules[ii][jj + 1]))

    print(newst)
    return (newst)

def concName(word):
    strg = ""

    for j in range(1, len(word)):
        strg = strg + word[j]

    if findStateWithName(strg) == "":
        return strg


def concState(word, name):
    newStt = ""

    print(word)
    print("W1: %s" % name)
    newStt = newStt + returnAllStates(name, word[0])

    print("Novostat: %s " % newStt)


def createNewState(word, name):
    concName(word)
    concState(word, name)

def testAFND(word, statsK):
    # First verification - Verify if all letters are in alphabet  #
    if verifyAllEntries(word) == False:
        print("The alphabet is wrong!")
        return



    for jj in statsK:
        for ii in jj.rules:
            if len(ii) > 2:
                print("------------------\nName: %s" % jj.name)
                createNewState(ii, jj.name)

