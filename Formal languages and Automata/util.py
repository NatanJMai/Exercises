#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stats import States

#q0 = States('q0', (('a', 'q0'), ('b', 'q1'), ('c', 'q2')), True, False ) # q0 Definition
#q1 = States('q1', (('a', 'q1'), ('b', 'q0'), ('c', 'q0')), False, False ) # q1 Definition
#q2 = States('q2', (('a', 'q0'), ('b', 'q0'), ('c', 'q0')), False, True) # q2 Definition
#statsK = (q0, q1, q2)

statsK  = ('S', 'a', 'ab', 'aba', 'abab')     # Set of states
alphbt  = ('a', 'b')        # alphabet
functi  = "func"                 # function
initiS  = 'S'                   # Init state
finalS  = 'abab'                   # Final states

S       = States('S'    , (('a', 'a')   , ('b', ''))     , True , False )
a       = States('a'    , (('a', 'a')   , ('b', 'ab'))   , False, False )
ab      = States('ab'   , (('a', 'aba') , ('b', 'S'))    , False, False )
aba     = States('aba'  , (('a', 'a')   , ('b', 'abab')) , False, False )
abab    = States('abab' , (('a', '')    , ('b', ''))     , False, True  )

statsK  = (S, a, ab, aba, abab)


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
    stateNow = statsK[0]

    for w in word:
        #print("actual state: %s" % stateNow.name)
        stateNow = returnNextState(w, stateNow)
        #if stateNow == "":
           # print("w-> %s, state -> not avail" % w)
        print("     w-> %s, state -> %s" %(w, stateNow.name))
        if stateNow.final == True:
            print("FINAL - ACEITO")
            return

    if stateNow.final == False:
        print("FINAL - REJEITO")
        return
