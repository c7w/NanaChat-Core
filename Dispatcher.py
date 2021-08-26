'''
Nana-Core: Dispatcher Module

+ Providing methods for sending messages
'''

from abc import abstractmethod, ABCMeta

class Dispatcher(ABCMeta):
    @abstractmethod
    def send():
        raise NotImplementedError

class DispatcherQQ(Dispatcher):
    def send():
        