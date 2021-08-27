'''
Nana-Core: Main Module
Under development...
'''

from Utils.Listener import MainListener
from Utils.Dispatcher import Dispatcher
from Utils.Interface import Action, Destination, MessageElement
from Utils.PluginManager import PluginManager


def Test1():
    # Load Configuration and Post actions
    pass


if __name__ == "__main__":
    PluginManager.AppStart()
    MainListener.run(host="0.0.0.0", port=5051)
