'''
Nana-Core: Interface Module

+ Define interfaces for use
'''

from enum import Enum
from typing import List
from abc import ABCMeta, abstractmethod

# Messages


class MessageType(Enum):
    TEXT = 1
    IMAGE = 2
    VOICE = 3
    VIDEO = 4


class MessageElement(metaclass=ABCMeta):

    def __init__(self, content):
        self.content = content

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    @abstractmethod
    def type(self) -> MessageType:
        raise NotImplementedError

    @staticmethod
    def fromPlainText(content):
        return MessagePlainText(content)

    @staticmethod
    def fromImage(content):
        return MessageImage(content)


class MessagePlainText(MessageElement):
    @property
    def type(self) -> MessageType:
        return MessageType.TEXT

    def __str__(self):
        return f"[MessagePlainText: {self.content}]"
    
    def toQQMessageChain(self):
        return {"type": "Plain", "text": f"{self.content}"}


class MessageImage(MessageElement):
    @property
    def type(self) -> MessageType:
        return MessageType.Image

    def __str__(self):
        return f"[MessageImage: {self.content}]"

    def toQQMessageChain(self):
        return {"type": "Image", "url": f"{self.content}"}

# Destination


class DestinationType(Enum):
    QQFriend = 1
    QQGroup = 2


class Destination(metaclass=ABCMeta):
    @property
    @abstractmethod
    def type(self) -> DestinationType:
        raise NotImplementedError

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    def __init__(self, content):
        self.content = content
    
    @staticmethod
    def fromQQFriend(content):
        return DestinationQQFriend(content)
    
    @staticmethod
    def fromQQGroup(content):
        return DestinationQQGroup(content)


class DestinationQQFriend(Destination):
    @property
    def type(self) -> DestinationType:
        return DestinationType.QQFriend

    def __str__(self):
        return f"[DestinationQQFriend {self.content}]"

class DestinationQQGroup(Destination):
    @property
    def type(self) -> DestinationType:
        return DestinationType.QQGroup

    def __str__(self):
        return f"[DestinationQQGroup {self.content}]"


# Dispatcher action
class Action():
    @property
    def message(self) -> List[MessageElement]:
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def destination(self) -> List[Destination]:
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value

    def __init__(self, message: List[MessageElement], destination: List[Destination]):
        self.message = message
        self.destination = destination
