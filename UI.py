'''
Created on Mar 29, 2017

@author: Madalina
'''
class UI:
    def __init__(self, ctrl):
        self._ctrl = ctrl;
        
    def start(self):
        stack = self._ctrl.hamiltonian()
        if stack == False:
            print("There are no hamiltonian cycles.")