'''
Nana-Core: Dispatcher Module

+ Providing methods for sending messages
'''

from Utils.Interface import Destination, DestinationQQFriend, DestinationQQGroup, DestinationType, Action, MessageElement
from Utils.PluginManager import PluginManager
from typing import List
import requests


class Dispatcher():
    @staticmethod
    def send(action: Action):
        SendStrategies = {
            DestinationType.QQFriend: DispatcherQQ.sendQQFriend,
            DestinationType.QQGroup: DispatcherQQ.sendQQGroup,
        }

        for destination in action.destination:
            SendStrategies[destination.type](destination, action.message)


class DispatcherQQ:
    @staticmethod
    def sendQQFriend(destination: DestinationQQFriend, messageList: List[MessageElement]):
        URL = PluginManager.CONFIGURATION['destinations']['QQ']['http-adapter-address']
        res = requests.post(URL+'/sendFriendMessage', headers={'Content-Type': 'application/json'},
                json={"target": destination.content, "messageChain": [message.toQQMessageChain() for message in messageList]})

    @staticmethod
    def sendQQGroup(destination: DestinationQQGroup, messageList: List[MessageElement]):
        URL = PluginManager.CONFIGURATION['destinations']['QQ']['http-adapter-address']
        res = requests.post(URL+'/sendGroupMessage', headers={'Content-Type': 'application/json'},
                            json={"target": destination.content, "messageChain": [message.toQQMessageChain() for message in messageList]})
