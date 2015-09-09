import string as S
import xlrd

class Automaton(object):
  def init(self, states):
    self.states = states


class State(object):
  def create(self, name, final):
    self.name  = name
    self.final = final
    self.rules = []

global automaton
automaton = Automaton()
automaton.init([])


def openFile():
  lines     = 86 
  colum     = 37
  workbook  = xlrd.open_workbook('compiladores.xls')
  wk        = workbook.sheet_by_name('Sheet1')
  
  for i in range(2, lines):
    name  = str(wk.cell(i, 1).value)
    final = False
    if str(wk.cell(i, 0).value) == '*':
      final = True
    
    state = State()
    state.create(name, final)
    
    for j in range(2, colum):
      state.rules.append((str(S.strip(wk.cell(1, j).value)), str(wk.cell(i, j).value)))
    
    automaton.states.append(state)
  
  return automaton


def findState(stt):
  for i in automaton.states:
    if i.name == stt:
      return i
  return ()


def nextState(atual, stg):
  for i in atual.rules:
    if i[0] == stg:
      return findState(i[1])
  return ()

def autMain():
  aut = openFile()
  return aut

if __name__ == "__main__":
  autMain()
