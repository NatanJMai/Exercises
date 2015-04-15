#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Automata - First implementation
#
# Desenvolver um programa que simule AFD's e AFND's e operações relacionadas.
# O programa deve dar a possibilidade do usuário escolher as seguintes opções:
#    1 – Fazer e testar um AFD;
#    2 – Fazer e testar um AFND;
#    3 – Converter um AFND para um AFD (teorema da determinização).
#    Nesse caso o programa deve verificar se a entrada já é um AFD
#    (dizendo que não precisa aplicar a determinização) ou
#        então deve aplicar a determinização e gerar o AFD resultante como saída.


#def afd():

from stats import States

statsK = ('q0', 'q1', 'q2')     # Set of states
alphbt = ('a', 'b', 'c')        # alphabet
functi = "func"                 # function
initiS = 'q0'                   # Init state
finalS = 'q2'                   # Final states


q0 = States('q0', (('a', 'q0'), ('b', 'q1'), ('c', 'q2'))) # q0 Definition
q1 = States('q1', (('a', 'q1'), ('b', 'q0'), ('c', 'q0'))) # q1 Definition
q2 = States('q2', (('a', 'q0'), ('b', 'q0'), ('c', 'q0'))) # q2 Definition


statsK = (q0, q1, q2)

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


def testAFD(entry, statsK):
    stateNow = statsK[0]

    stateNow = returnNextState('c', stateNow)

    if stateNow != "":
        print(stateNow.name)


def main():

    # Statics   - Entry static #
    entry = 'aaabbb'

    # First verification - Verify if all letters are on alphabet  #
    if verifyAllEntries(entry) == False:
        print("false")
        return

    for stt in statsK:
        print("%s => %s" % (str(stt.name), str(stt.rules)))

    testAFD(entry, statsK)


if __name__ == '__main__':
    main()
