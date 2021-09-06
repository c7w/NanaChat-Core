# Client.py
from Utils.Listener import Listener
from Utils.Interface import *
import json
import asyncio
import datetime
from typing import List, Dict
import websockets

def parseMessageChain(messageChain: List[Dict]):
    MessageElementList = []
    for message in messageChain:
        # TODO: parse message
        if message['type'] == 'Image':
            MessageElementList.append(MessageImage(message['url']))
        if message['type'] == 'Plain':
            MessageElementList.append(MessagePlainText(message['text']))
    return MessageElementList

class ExtensionQQ(object):
    
    BufferList = []
    syncId = 0
    
    @staticmethod
    async def recv(websocket):
        while True:
            recv = await websocket.recv()
            recv = json.loads(recv)
            data = recv['data']
            if data.get('type'):
                if data['type'] == "FriendMessage":
                    Listener.notifyAll(Action(parseMessageChain(data['messageChain']), [DestinationQQFriend(data['sender']['id'])]))
                if data['type'] == 'GroupMessage':
                    Listener.notifyAll(Action(parseMessageChain(data['messageChain']), [DestinationQQGroup(data['sender']['group']['id'])]))

    @staticmethod
    async def send(websocket):
        while True:
            # Send
            if len(ExtensionQQ.BufferList) > 0:
                data = ExtensionQQ.BufferList.pop()
                await websocket.send(data)
            await asyncio.sleep(0.2)

    @staticmethod
    def sendFriendMessage(destination: DestinationQQFriend, messageList: List[MessageElement]):
        data = {}
        ExtensionQQ.syncId += 1
        data['syncId'] = ExtensionQQ.syncId
        data['command'] = "sendFriendMessage"
        content = {}
        content['target'] = destination.content
        content['messageChain'] = []
        for message in messageList:
            if message.type == MessageType.TEXT:
                content['messageChain'].append({"type": "Plain", "text": f"{message.content}"})
            if message.type == MessageType.IMAGE:
                content['messageChain'].append({"type": "Image", "url": f"{message.content}"})
        data['content'] = content
        ExtensionQQ.BufferList.append(json.dumps(data, ensure_ascii=False))
    
    @staticmethod 
    def sendGroupMessage(destination: DestinationQQGroup, messageList: List[MessageElement]):
        data = {}
        ExtensionQQ.syncId += 1
        data['syncId'] = ExtensionQQ.syncId
        data['command'] = "sendGroupMessage"
        content = {}
        content['target'] = destination.content
        content['messageChain'] = []
        for message in messageList:
            if message.type == MessageType.TEXT:
                content['messageChain'].append({
                    "type": "Plain", "text": f"{message.content}"})
            if message.type == MessageType.IMAGE:
                content['messageChain'].append({
                    "type": "Image", "url": f"{message.content}"})
        data['content'] = content
        ExtensionQQ.BufferList.append(json.dumps(data, ensure_ascii=False))
    
    @staticmethod
    async def socket(uri):
        async with websockets.connect(uri) as websocket:
            print("[Websocket QQ] Connected successfully!")
            await asyncio.gather(ExtensionQQ.recv(websocket), ExtensionQQ.send(websocket))
