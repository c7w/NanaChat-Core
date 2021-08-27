'''
Nana-Core: PluginManager Module

+ Loading Configurations
+ Manage Global variables
+ Manage Plugins
'''

import yaml

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
        print(PluginManager.CONFIGURATION)
        # TODO: Register plugins...
