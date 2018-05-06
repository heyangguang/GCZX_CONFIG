from backend.edit import Edit_Congif
from backend.userinput import User_Input

class expert(object):

    def __init__(self,location = '/expert/WEB-INF/classes/'):
        self.location = location
        self.user_input = User_Input()
        self.user_input.input_user()
        self.user_input.input_cas_config()
        self.user_input.input_db_config()
        self.user_input.input_project_config()
        self.user_input.input_ip_port_config()

    # jeesite.properties
    def je_properties(self):
        old_str = 'jeesite.properties'
        location_str = self.user_input.location
        find_list = ['cas.server.url','cas.project.url','jdbc.url']

        for find_str in find_list:
            if self.user_input.config.get(find_str):
                if find_str == 'cas.project.url':
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str] + 'expert').Globa_Edit()
                else:
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str]).Globa_Edit()

    # raqreport.properties
    def ra_properties(self):
        old_str = 'raqreport.properties'
        location_str = self.user_input.location

        Edit_Congif(location_str+self.location+old_str,
                    new_str=self.user_input.ip_port).Re_Edit()

    # systemUrl.properties
    def sy_properties(self):
        old_str = 'systemUrl.properties'
        location_str = self.user_input.location

        Edit_Congif(location_str+self.location+old_str,
                    new_str=self.user_input.ip_port).Re_Edit()


class acb(object):

    def __init__(self,location = '/acb/WEB-INF/classes/'):
        self.location = location
        self.user_input = User_Input()
        self.user_input.input_user()
        self.user_input.input_cas_config()
        self.user_input.input_db_config()
        self.user_input.input_project_config()
        self.user_input.input_ip_port_config()
        self.user_input.input_bpm_config()
        self.user_input.input_superMap_config()
        self.user_input.input_redis_config()

    # jeesite.properties
    def je_properties(self):
        old_str = 'jeesite.properties'
        location_str = self.user_input.location
        find_list = ['cas.server.url','cas.project.url','jdbc.url']

        for find_str in find_list:
            if self.user_input.config.get(find_str):
                if find_str == 'cas.project.url':
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str] + 'acb').Globa_Edit()
                else:
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str]).Globa_Edit()

    # raqreport.properties
    def ra_properties(self):
        old_str = 'acbReport.properties'
        location_str = self.user_input.location

        Edit_Congif(location_str+self.location+old_str,
                    new_str=self.user_input.ip_port).Re_Edit()

    # systemUrl.properties
    def sy_properties(self):
        old_str = 'systemUrl.properties'
        location_str = self.user_input.location

        Edit_Congif(location_str+self.location+old_str,
                    new_str=self.user_input.ip_port).Re_Edit()

        find_list = ['bpmUrl','superMapUrl']
        for find_str in find_list:
            if self.user_input.acb_config.get(find_str):
                Edit_Congif(location_str+self.location+old_str,find_str,
                            self.user_input.acb_config[find_str]).Globa_Edit()

    def redis_conf(self):
        old_str = 'spring-context-jedis.xml'
        location_str = self.user_input.location
        find_str = 'bean'

        Edit_Congif(location_str + self.location + old_str, find_str,
                    self.user_input.redis).Xml_Redis2()


class acbplat(object):

    def __init__(self,location = '/acbplat/WEB-INF/classes/'):
        self.location = location
        self.user_input = User_Input()
        self.user_input.input_user()
        self.user_input.input_cas_config()
        self.user_input.input_db_config()
        self.user_input.input_project_config()
        self.user_input.input_ip_port_config()

    # jeesite.properties
    def je_properties(self):
        old_str = 'jeesite.properties'
        location_str = self.user_input.location
        find_list = ['cas.server.url','cas.project.url','jdbc.url']

        for find_str in find_list:
            if self.user_input.config.get(find_str):
                if find_str == 'cas.project.url':
                    Edit_Congif(location_str+self.location+old_str,find_str,
                                self.user_input.config[find_str]+'acbplat').Globa_Edit()
                else:
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str]).Globa_Edit()

    # systemUrl.properties
    def sy_properties(self):
        old_str = 'systemUrl.properties'
        location_str = self.user_input.location

        Edit_Congif(location_str+self.location+old_str,
                    new_str=self.user_input.ip_port).Re_Edit()


class demonarea(object):

    def __init__(self,location = '/demonarea/WEB-INF/classes/'):
        self.location = location
        self.user_input = User_Input()
        self.user_input.input_user()
        self.user_input.input_cas_config()
        self.user_input.input_db_config()
        self.user_input.input_project_config()
        self.user_input.input_ip_port_config()
        self.user_input.input_superMap_config()
        self.user_input.input_bas5Url_config()

    # jeesite.properties
    def je_properties(self):
        old_str = 'jeesite.properties'
        location_str = self.user_input.location
        find_list = ['cas.server.url','cas.project.url','jdbc.url']

        for find_str in find_list:
            if self.user_input.config.get(find_str):
                if find_str == 'cas.project.url':
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str] + 'demonarea').Globa_Edit()
                else:
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str]).Globa_Edit()

    # raqreport.properties
    def ra_properties(self):
        old_str = 'raqreport.properties'
        location_str = self.user_input.location

        Edit_Congif(location_str+self.location+old_str,
                    new_str=self.user_input.ip_port).Re_Edit()

    # systemUrl.properties
    def sy_properties(self):
        old_str = 'systemUrl.properties'
        location_str = self.user_input.location

        Edit_Congif(location_str+self.location+old_str,
                    new_str=self.user_input.ip_port).Re_Edit()

        find_list = ['bas5Url','superMapUrl']
        for find_str in find_list:
            if self.user_input.demonarea_config.get(find_str):
                Edit_Congif(location_str+self.location+old_str,find_str,
                            self.user_input.demonarea_config[find_str]).Globa_Edit()


class serviceMana(object):

    def __init__(self,location = '/serviceMana/WEB-INF/classes/'):
        self.location = location
        self.user_input = User_Input()
        self.user_input.input_user()
        self.user_input.input_cas_config()
        self.user_input.input_db_config()
        self.user_input.input_project_config()
        self.user_input.input_ip_port_config()

    # jeesite.properties
    def je_properties(self):
        old_str = 'jeesite.properties'
        location_str = self.user_input.location
        find_list = ['cas.server.url','cas.project.url','jdbc.url']

        for find_str in find_list:
            if self.user_input.config.get(find_str):
                if find_str == 'cas.project.url':
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str] + 'serviceMana').Globa_Edit()
                else:
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str]).Globa_Edit()

    # systemUrl.properties
    def sy_properties(self):
        old_str = 'systemUrl.properties'
        location_str = self.user_input.location

        Edit_Congif(location_str+self.location+old_str,
                    new_str=self.user_input.ip_port).Re_Edit()


class support(object):

    def __init__(self,location = '/support/WEB-INF/classes/'):
        self.location = location
        self.user_input = User_Input()
        self.user_input.input_user()
        self.user_input.input_cas_config()
        self.user_input.input_db_config()
        self.user_input.input_project_config()
        self.user_input.input_ip_port_config()
        self.user_input.input_superMap_config()

    # jeesite.properties
    def je_properties(self):
        old_str = 'jeesite.properties'
        location_str = self.user_input.location
        find_list = ['cas.server.url','cas.project.url','jdbc.url']

        for find_str in find_list:
            if self.user_input.config.get(find_str):
                if find_str == 'cas.project.url':
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str] + 'support').Globa_Edit()
                else:
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str]).Globa_Edit()

    # raqreport.properties
    def ra_properties(self):
        old_str = 'raqreport.properties'
        location_str = self.user_input.location

        Edit_Congif(location_str+self.location+old_str,
                    new_str=self.user_input.ip_port).Re_Edit()

    # systemUrl.properties
    def sy_properties(self):
        old_str = 'systemUrl.properties'
        location_str = self.user_input.location

        Edit_Congif(location_str+self.location+old_str,
                    new_str=self.user_input.ip_port).Re_Edit()

        find_str = 'superMapUrl'
        Edit_Congif(location_str + self.location + old_str, find_str,
                    self.user_input.acb_config[find_str]).Globa_Edit()


class uams(object):

    def __init__(self,location = '/uams/WEB-INF/classes/'):
        self.location = location
        self.user_input = User_Input()
        self.user_input.input_user()
        self.user_input.input_cas_config()
        self.user_input.input_db_config()
        self.user_input.input_project_config()
        self.user_input.input_ip_port_config()
        self.user_input.input_bpm_config()
        self.user_input.input_continuedDevbpmUrl_config()
        self.user_input.input_modernAgriDemobpmUrl_config()
        self.user_input.input_modernAgriIndusParkbpmUrl_config()

    # jeesite.properties
    def je_properties(self):
        old_str = 'jeesite.properties'
        location_str = self.user_input.location
        find_list = ['cas.server.url','cas.project.url','jdbc.url']

        for find_str in find_list:
            if self.user_input.config.get(find_str):
                if find_str == 'cas.project.url':
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str] + 'uams').Globa_Edit()
                else:
                    Edit_Congif(location_str + self.location + old_str, find_str,
                                self.user_input.config[find_str]).Globa_Edit()

    # systemUrl.properties
    def sy_properties(self):
        old_str = 'systemUrl.properties'
        location_str = self.user_input.location

        Edit_Congif(location_str+self.location+old_str,
                    new_str=self.user_input.ip_port).Re_Edit()

        find_list = ['bpmUrl', 'modernAgriDemobpmUrl', 'continuedDevbpmUrl', 'modernAgriIndusParkbpmUrl']
        for find_str in find_list:
            if self.user_input.uams_config.get(find_str):
                Edit_Congif(location_str + self.location + old_str, find_str,
                            self.user_input.uams_config[find_str]).Globa_Edit()


class report(object):

    def __init__(self,location = '/report/WEB-INF/classes/',
                 xml_location='/report/WEB-INF/'):
        self.location = location
        self.xml_location = xml_location
        self.user_input = User_Input()
        self.user_input.input_db_config()
        self.user_input.input_appUrlPrefix_config()
        self.user_input.input_user()

    # raqsoftConfig.xml
    def xml_raqsoftConfig(self):
        old_str = 'raqsoftConfig.xml'
        location_str = self.user_input.location
        find_str = 'property'

        Edit_Congif(location_str+self.xml_location+old_str,find_str,
                    self.user_input.config['jdbc.url']).Xml_Edit\
            (self.user_input.report_config['appUrlPrefix'])

    # dbcp.properties
    def dbcp_properties(self):
        old_str = 'dbcp.properties'
        location_str = self.user_input.location
        find_str = 'url'

        Edit_Congif(location_str+self.location+old_str,find_str,
                    self.user_input.config['jdbc.url']).Globa_Edit()

    # jdbc.properties
    def jdbc_properties(self):
        old_str = 'jdbc.properties'
        location_str = self.user_input.location
        find_str = 'db.url'

        Edit_Congif(location_str+self.location+old_str,find_str,
                    self.user_input.config['jdbc.url']).Globa_Edit()


class cas(object):

    def __init__(self,location = '/cas/WEB-INF/',
                 jsp_location='/cas/WEB-INF/view/jsp/default/ui/',
                 redis_cluster_location='/cas/WEB-INF/spring-configuration/'):
        self.location = location
        self.jsp_location = jsp_location
        self.redis_cluster_location = redis_cluster_location
        self.user_input = User_Input()
        self.user_input.input_user()
        self.user_input.input_db_config()
        self.user_input.input_casLoginView_config()
        self.user_input.input_redis_config()

    # jdbc.properties
    def jdbc_properties(self):
        old_str = 'jdbc.properties'
        location_str = self.user_input.location
        find_str = 'jdbc.url'

        Edit_Congif(location_str+self.location+old_str,find_str,
                    self.user_input.config['jdbc.url']).Globa_Edit()

    # casLoginView.jsp
    def jsp_casLoginView(self):
        old_str = 'casLoginView.jsp'
        location_str = self.user_input.location
        re = '(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]):{0,1}\d{0,6}(?!/acbplat)'

        Edit_Congif(location_str+self.jsp_location+old_str,
                    new_str=self.user_input.cas_config['casLoginView']).Re_Edit(re1=re)

    def redis_cluster_conf(self):
        old_str = 'ticketRegistry.xml'
        location_str = self.user_input.location
        find_str = 'constructor-arg'

        Edit_Congif(location_str + self.redis_cluster_location + old_str,
                    find_str, new_str=self.user_input.redis).Xml_Redis()