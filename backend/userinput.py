from readconfig.read_ini import Read_Config_Ini

class User_Input(object):
    '''获取config.ini配置文件'''

    def __init__(self,location='',config={},ip_port='',acb_config={},
                 demonarea_config={},support_config={},uams_config={},
                 report_config={},cas_config={},app_config={},redis=''):
        self.read_config_ini = Read_Config_Ini()
        self.location = location
        self.config = config
        self.ip_port = ip_port
        self.acb_config = acb_config
        self.demonarea_config = demonarea_config
        self.support_config = support_config
        self.uams_config = uams_config
        self.report_config = report_config
        self.cas_config = cas_config
        self.app_config = app_config
        self.redis = redis

    def input_user(self):
        self.location = self.read_config_ini.getConfigValue('ProjectLocation')

    def input_cas_config(self):
        self.config['cas.server.url'] = self.read_config_ini.getConfigValue('CasUrl')

    def input_db_config(self):
        self.config['jdbc.url'] = self.read_config_ini.getConfigValue('JDBC')

    def input_project_config(self):
        self.config['cas.project.url'] = self.read_config_ini.getConfigValue('ProjectUrl')

    def input_ip_port_config(self):
        self.ip_port = self.read_config_ini.getConfigValue('IpPort')

    def input_bpm_config(self):
        self.acb_config['bpmUrl'] = self.read_config_ini.getConfigValue('BpmUrl')
        self.uams_config['bpmUrl'] = self.read_config_ini.getConfigValue('BpmUrl')

    def input_superMap_config(self):
        self.acb_config['superMapUrl'] = self.read_config_ini.getConfigValue('SuperMapUrl')
        self.demonarea_config['superMapUrl'] = self.read_config_ini.getConfigValue('SuperMapUrl')
        self.support_config['superMapUrl'] = self.read_config_ini.getConfigValue('SuperMapUrl')

    def input_bas5Url_config(self):
        self.demonarea_config['bas5Url'] = self.read_config_ini.getConfigValue('Bas5Url')

    def input_modernAgriDemobpmUrl_config(self):
        self.uams_config['modernAgriDemobpmUrl'] = self.read_config_ini.getConfigValue('modernAgriDemobpmUrl')

    def input_continuedDevbpmUrl_config(self):
        self.uams_config['continuedDevbpmUrl'] = self.read_config_ini.getConfigValue('continuedDevbpmUrl')

    def input_modernAgriIndusParkbpmUrl_config(self):
        self.uams_config['modernAgriIndusParkbpmUrl'] = self.read_config_ini.getConfigValue('modernAgriIndusParkbpmUrl')

    def input_appUrlPrefix_config(self):
        self.report_config['appUrlPrefix'] = self.read_config_ini.getConfigValue('appUrlPrefix')

    def input_casLoginView_config(self):
        self.cas_config['casLoginView'] = self.read_config_ini.getConfigValue('casLoginView')

    def input_appCconfig_config(self):
        self.app_config['expert'] = self.read_config_ini.getAppConfigValue('expert')
        self.app_config['acb'] = self.read_config_ini.getAppConfigValue('acb')
        self.app_config['acbplat'] = self.read_config_ini.getAppConfigValue('acbplat')
        self.app_config['demonarea'] = self.read_config_ini.getAppConfigValue('demonarea')
        self.app_config['serviceMana'] = self.read_config_ini.getAppConfigValue('serviceMana')
        self.app_config['support'] = self.read_config_ini.getAppConfigValue('support')
        self.app_config['uams'] = self.read_config_ini.getAppConfigValue('uams')
        self.app_config['report'] = self.read_config_ini.getAppConfigValue('report')
        self.app_config['cas'] = self.read_config_ini.getAppConfigValue('cas')

    def input_redis_config(self):
        self.redis = self.read_config_ini.getRedisConfigValue('url')