'''
Nana-Core: PluginManager Module

+ Loading Configurations
+ Manage Global variables
+ Manage Plugins
'''

import os
import asyncio
import yaml
from Utils.extensions import WebSocketQQ

class PluginManager:
    CONFIGURATION = {}

    # Configurations
    @staticmethod
    def LoadConfiguration():
        file = open("Config.yml", "r", encoding='utf-8')
        PluginManager.CONFIGURATION = yaml.load(file, Loader=yaml.FullLoader)
        file.close()

    @staticmethod
    def AppStart():
        PluginManager.LoadConfiguration()
        # TODO: Register plugins...
        for pluginName in os.listdir('./plugins/'):
            if (not pluginName.startswith('_')) and pluginName.endswith('.py'):
                __import__('plugins.' + pluginName[:-3])
        
        coroutines = asyncio.gather(WebSocketQQ.ExtensionQQ.socket(
            PluginManager.CONFIGURATION['destinations']['QQ']['ws-adapter-address']))
        asyncio.get_event_loop().run_until_complete(coroutines)
