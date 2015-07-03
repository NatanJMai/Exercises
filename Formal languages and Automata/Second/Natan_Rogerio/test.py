#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Linguagens formais e automatos
# Natan J. Mai - Rogerio Torchelsen
# Ciencia da Computacao  - Universidade Federal da Fronteira Sul
# 6º semestre

# Para executar os testes, basta criar
# uma funcao e chama-la no arquivo test.py.
# Apos criar a funcao, chamar na funcao tests()
# Estrutura da glc = [[producoes], [producoes], [producoes]  
# Exemplo: glc = [["A -> b | c"], ["B -> d | e"]]
 
# Deixar os espacos exatamente como mostrado no exemplo.
# Simb maiusculos sao os nao terminais.
# Simb minusculos sao os terminais.

# Para rodar: python test.py
# Plataforma desenvolvida: Fedora - Python 2.7.5

import time
import os
from lfa import main

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def test1():
  glci  = [["A -> B | C | D | a"], 
           ["B -> b"], 
           ["C -> c"], 
           ["D -> d"]]
  main(glci)

def test2():
  glci  = [["S -> Tb | a | xT | Co | Ep |Eo | E"], 
           ["T -> o"], 
           ["C -> w"], 
           ["D -> i"], 
           ["E -> $ | e | T"], 
           ["F -> f"], 
           ["G -> gig | S"]]
  main(glci)

def test3():
  glci  = [["X -> YZ | aY | bY | z | c"], 
           ["Y -> a"], 
           ["Z -> $"]]
  main(glci)

def tests():
  while True:
    clear()
    v = int(raw_input("Op (1, 2, 3) > "))
  
    if v == 1:
      print("TEST 01 =>\n")
      test1()
    elif v == 2:
      print("TEST 02 =>\n")
      test2()
    elif v == 3:
      print("TEST 03 =>\n")
      test3()
    raw_input("\n\n\n\nPRESS ENTER ---->")
if __name__ == "__main__":
  tests()
