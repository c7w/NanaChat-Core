'''
Nana-Core: Main Module
Under development...
'''
from Utils.Interface import Action, Destination, MessageElement
from Utils.Dispatcher import Dispatcher
from Utils.PluginManager import PluginManager


def Test1():
    # Load Configuration and Post actions
    pass


Dispatcher.send(Action([MessageElement.fromPlainText('Bot 启动 咕咕咕\n')], [
                Destination.fromQQGroup(683950981)]))
if __name__ == "__main__":
    PluginManager.AppStart()
    
