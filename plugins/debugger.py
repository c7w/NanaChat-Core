from Utils.Interface import *
from Utils.Listener import Listener
from Utils.Dispatcher import Dispatcher

def notify(action: Action):
    # Filter sender QQ 

    for destination in action.destination:
        if destination.type == DestinationType.QQFriend and destination.content == 1291459906:
            action.message.insert(0, MessagePlainText("[Debug Message]"))
            action = Action(action.message, [DestinationQQGroup(683950981)])
            Dispatcher.send(action)

main = Listener("Debugger.main", notify, True)
Listener.registerListener(main)
