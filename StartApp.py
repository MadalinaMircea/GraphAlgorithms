'''
Created on Mar 29, 2017

@author: Madalina
'''

from Repository import Repository
from Controller import Controller
from UI import UI

repo = Repository()
ctrl = Controller(repo)
ui = UI(ctrl)

ui.start()