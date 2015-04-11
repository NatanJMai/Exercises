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
q1 = States('q1', (('a', 'q1'), ('b', 'q2'), ('c', 'q2'))) # q1 Definition
q2 = States('q2', (('a', 'q2'), ('b', 'q2'), ('c', 'q2'))) # q2 Definition


statsK = (q0, q1, q2)

def verifyEntry(entry):
    for j in entry:
        if not j in alphbt:
            return False

def main():

    # Statics   - Entry static #
    entry = 'aaabbb'

    # First verification - Verify if all letters are on alphabet  #
    if verifyEntry(entry) == False:
        print("false")
        return

    for stt in statsK:
        print("%s => %s" % (str(stt.name), str(stt.rules)))



if __name__ == '__main__':
    main()
