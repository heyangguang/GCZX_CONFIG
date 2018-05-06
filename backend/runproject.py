from backend import file_classification
from backend.userinput import User_Input
import time

class expert_project(object):
    '''调用expert项目所有更改'''

    def __init__(self):
        time.sleep(0.5)
        u = User_Input()
        u.input_appCconfig_config()
        if u.app_config['expert']:
            expert = file_classification.expert()
            expert.je_properties()
            expert.ra_properties()
            expert.sy_properties()
            print('expert修改执行成功')
        else:
            print('expert修改未执行(状态码0)')


class acb_project(object):
    '''调用acb项目所有更改'''

    def __init__(self):
        time.sleep(0.5)
        u = User_Input()
        u.input_appCconfig_config()
        if u.app_config['acb']:
            acb = file_classification.acb()
            acb.je_properties()
            acb.ra_properties()
            acb.sy_properties()
            acb.redis_conf()
            print('acb修改执行成功')
        else:
            print('acb修改未执行(状态码0)')


class acbplat_priject(object):
    '''调用acbplat项目所有更改'''

    def __init__(self):
        time.sleep(0.5)
        u = User_Input()
        u.input_appCconfig_config()
        if u.app_config['acbplat']:
            acbplat = file_classification.acbplat()
            acbplat.sy_properties()
            acbplat.je_properties()
            print('acbplat修改执行成功')
        else:
            print('acbplat修改未执行(状态码0)')

class demonarea_project(object):
    '''调用demonarea项目所有更改'''

    def __init__(self):
        time.sleep(0.5)
        u = User_Input()
        u.input_appCconfig_config()
        if u.app_config['demonarea']:
            demonarea = file_classification.demonarea()
            demonarea.je_properties()
            demonarea.ra_properties()
            demonarea.sy_properties()
            print('demonarea修改执行成功')
        else:
            print('demonarea修改未执行(状态码0)')

class serviceMana_project(object):
    '''调用serviceMana项目所有更改'''

    def __init__(self):
        time.sleep(0.5)
        u = User_Input()
        u.input_appCconfig_config()
        if u.app_config['serviceMana']:
            serviceMana = file_classification.serviceMana()
            serviceMana.je_properties()
            serviceMana.sy_properties()
            print('serviceMana修改执行成功')
        else:
            print('serviceMana修改未执行(状态码0)')

class support_project(object):
    '''调用support项目所有更改'''

    def __init__(self):
        time.sleep(0.5)
        u = User_Input()
        u.input_appCconfig_config()
        if u.app_config['support']:
            support = file_classification.support()
            support.je_properties()
            support.sy_properties()
            support.ra_properties()
            print('support修改执行成功')
        else:
            print('support修改未执行(状态码0)')

class uams_project(object):
    '''调用uams项目所有更改'''

    def __init__(self):
        time.sleep(0.5)
        u = User_Input()
        u.input_appCconfig_config()
        if u.app_config['uams']:
            uams = file_classification.uams()
            uams.sy_properties()
            uams.je_properties()
            print('uams修改执行成功')
        else:
            print('uams修改未执行(状态码0)')

class report_project(object):
    '''调用report项目所有更改'''

    def __init__(self):
        time.sleep(0.5)
        u = User_Input()
        u.input_appCconfig_config()
        if u.app_config['report']:
            report = file_classification.report()
            report.xml_raqsoftConfig()
            report.dbcp_properties()
            report.jdbc_properties()
            print('report修改执行成功')
        else:
            print('report修改未执行(状态码0)')

class cas_project(object):
    '''调用cas项目所有更改'''

    def __init__(self):
        time.sleep(0.5)
        u = User_Input()
        u.input_appCconfig_config()
        if u.app_config['cas']:
            cas = file_classification.cas()
            cas.jdbc_properties()
            cas.jsp_casLoginView()
            cas.redis_cluster_conf()
            print('cas修改执行成功')
        else:
            print('cas修改未执行(状态码0)')