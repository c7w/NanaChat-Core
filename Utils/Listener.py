from abc import ABC, abstractmethod
from typing import Callable
from Utils.PluginManager import PluginManager
from Utils.Interface import Action
from os import stat


'''
Nana-Core: **Listener** Module

+ Listener class
'''


class Listener():
    PluginListeners = []
    
    def __init__(self, uniqueId: str, notify: Callable[[Action], None], enabled=True):
        self.uniqueId = uniqueId
        self.notify = notify
        self.enabled = enabled
        
    @staticmethod
    def notifyAll(action: Action):
        for listener in Listener.PluginListeners:
            if listener.enabled ==  True:
                listener.notify(action)

    @staticmethod
    def getListenerById(uniqueId):
        for listener in Listener.PluginListeners:
            if listener.uniqueId == uniqueId:
                return listener
        return None

    @staticmethod
    def registerListener(listener):
        Listener.PluginListeners.append(listener)
