'''
Nana-Core: Dispatcher Module

+ Providing methods for sending messages
'''

from Utils.extensions.WebSocketQQ import ExtensionQQ
from Utils.Interface import Destination, DestinationQQFriend, DestinationQQGroup, DestinationType, Action
from Utils.PluginManager import PluginManager
from typing import List


class Dispatcher():

    SendStrategies = {
        DestinationType.QQFriend: ExtensionQQ.sendFriendMessage,
        DestinationType.QQGroup: ExtensionQQ.sendGroupMessage,
    }

    @staticmethod
    def send(action: Action):
        for destination in action.destination:
            Dispatcher.SendStrategies[destination.type](destination, action.message)
