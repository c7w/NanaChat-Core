'''
Nana-Core: Main Module
Under development...
'''

from Utils.Dispatcher import Dispatcher
from Utils.Interface import Action, Destination, MessageElement
from Utils.PluginManager import PluginManager


def Test1():
    # Load Configuration and Post actions
    pass


if __name__ == "__main__":
    PluginManager.AppStart()
    print(2)
    action = Action([MessageElement.fromPlainText("123")], [Destination.fromQQGroup(683950981)])
    Dispatcher.send(action)