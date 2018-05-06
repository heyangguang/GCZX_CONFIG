import time

class ArgvHandler(object):
    """接收用户参数，并调用相应的功能"""
    def __init__(self,sys_args):
        self.sys_args = sys_args

    def help_msg(self,error_msg=''):
        """帮助信息"""
        msgs = """
        %s
        run  启动更改
        """ % error_msg
        exit(msgs)


    def call(self):
        """根据用户参数，调用对应的方法"""
        if len(self.sys_args) == 1:
            self.help_msg("没有调用任何参数")

        if hasattr(self,self.sys_args[1]):
            func = getattr(self,self.sys_args[1])
            func()
        else:
            self.help_msg("没有方法:%s" %self.sys_args[1])


    def run(self):
        """启动用户交互程序"""
        from backend import runproject
        print('''
        HY，HY，HY，HY，HY，HY，HY，HY，HY，HY，HY，HY，HY，HY
        ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
        ,"                      ,"|        ,"        ,"  |
        +-----------------------+  |      ,"        ,"    |
        |  .-----------------.  |  |     +---------+      |
        |  |                 |  |  |     | -==----'|      |
        |  |  I LOVE GUN!    |  |  |     |         |      |
        |  |  Bad command or |  |  |/----|`---=    |      |
        |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
        |  |                 |  |  |  // |(((( [33]|    ,"
        |  `-----------------'  |," .;'| |((((     |  ,"
        +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
        ___________________________/___  `,
        /  oooooooooooooooo  .o.  oooo /,   \,"-----------
        / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
        /_==__==========__==_ooo__ooo=_/'   /___________,"
             ''')
        time.sleep(0.5)
        runproject.acb_project()
        runproject.acbplat_priject()
        runproject.cas_project()
        runproject.demonarea_project()
        runproject.expert_project()
        runproject.report_project()
        runproject.serviceMana_project()
        runproject.support_project()
        runproject.uams_project()