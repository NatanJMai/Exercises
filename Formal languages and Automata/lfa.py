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

from states import States
from util   import *

#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 01/05/2015
#   FILE : lfa.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Main function.
#------------------------------------------------------------
def main():
    testes()


if __name__ == '__main__':
    main()

