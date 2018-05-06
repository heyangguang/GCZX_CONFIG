import configparser

class Read_Config_Ini(object):

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read('config.ini')

    def getConfigValue(self, name):
        value = self.cf.get('Config', name)
        return value

    def getAppConfigValue(self, name):
        value = self.cf.get('AppConfig', name)
        return int(value)

    def getRedisConfigValue(self, name):
        value = self.cf.get('redis_cluster', name)
        return value