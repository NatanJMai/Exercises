#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stats import States

#q0 = States('q0', (('a', 'q0'), ('b', 'q1'), ('c', 'q2')), True, False ) # q0 Definition
#q1 = States('q1', (('a', 'q1'), ('b', 'q0'), ('c', 'q0')), False, False ) # q1 Definition
#q2 = States('q2', (('a', 'q0'), ('b', 'q0'), ('c', 'q0')), False, True) # q2 Definition
#statsK = (q0, q1, q2)

statsK  = ('q0', 'q1', 'q2', 'qf')    # Set of states
alphbt  = ('a', 'b')                            # alphabet

q0      = States('q0'   , (('a', 'q0', 'q1')       , ('b', 'q0', 'q2'))  , True , False )
q1      = States('q1'   , (('a', 'qf')             , ('b', ''))    , False, False )
q2      = States('q2'   , (('a', '' )              , ('b', 'qf'))    , False, False )
qf      = States('qf'   , (('a', 'qf')             , ('b', 'qf'))    , False, True  )

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

##
## @TODO
## * Criar os estados
## * Criar as regras para cada estado
## * Organizar os estados

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


def returnAllStates(state, letter):
    stt   = findStateWithName(state)
    newst = []
    full  = []
    nextStates = returnStatesWhenALetter(state, letter)

    if stt == "" or nextStates == "":
        return

    for jj in nextStates:
        newst.append(returnStatesWhenALetter(jj, letter))

    for hh in newst:
        for ii in hh:
            full.append(ii)

    #print(nextStates)
    return (full)


def concName(word):
    strg = ""

    for j in range(1, len(word)):
        strg = strg + word[j]

    if findStateWithName(strg) == "":
        return strg


def concState(word, letter):
    print("Word: %s" % str(word))
    print("Letter: %s" % letter)

    for jj in range(1, len(word)):
        return (returnAllStates(word[jj], letter))


def createNewState(word, name):
    newState = concName(word)
    print("NewState: %s " % newState)

    rules    = concState(word, word[0][0])
    print("Rules (%s) => %s" % (word[0][0], rules))



def testAFND(word, statsK):
    # First verification - Verify if all letters are in alphabet  #
    if verifyAllEntries(word) == False:
        print("The alphabet is wrong!")
        return

    for jj in statsK:
        for ii in jj.rules:
            if len(ii) > 2:
                print("------------------\n")
                createNewState(ii, jj.name)

