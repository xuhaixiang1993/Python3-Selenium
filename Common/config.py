import os
import configparser

import getcwd
from Common.log import log1
from Common.configOverWriter import ConfigOverWrite

path = getcwd.get_cwd()
# 配置文件路径
config_path = os.path.join(path, 'config.ini')
# 初始化操作配置文件实例
config = ConfigOverWrite()
# 读取配置文件
config.read(config_path, encoding='utf-8-sig')


class Config:
    @staticmethod
    def config_read(section, key):
        """从配置文件中读值"""
        # 读取seciton下key的value
        config.read(config_path, encoding='utf-8-sig')
        config_get = config.get(section, key)
        log1.info('在section：%s下读取%s的值' % (section, key))
        return config_get

    @staticmethod
    def config_write(section, key=None, value=None):
        """往配置文件写入"""
        # 在section下写入key, value
        if key is not None and value is not None:
            config.set(section, key, value)
            log1.info('在section：%s下新增%s=%s' % (section, key, value))
            with open(config_path, 'w', encoding='utf-8') as f:
                config.write(f)
        else:
            # 新增section
            config.add_section(section)
            log1.info("新增section：%s" % section)
            with open(config_path, 'w', encoding='utf-8') as f:
                config.write(f)

    @staticmethod
    def config_delete(section, key=None):
        """从配置文件中删除"""
        # 删除section下对应key, value
        if key is not None:
            config.remove_option(section, key)
            log1.info('删除section:%s下%s和他的值' % (section, key))
            with open(config_path, 'w', encoding='utf-8') as f:
                config.write(f)
        else:
            # 删除section
            config.remove_section(section)
            log1.info('删除section:%s' % section)
            with open(config_path, 'w', encoding='utf-8') as f:
                config.write(f)

    def config_options(self, section):
        '''读取配置文件某section下所有键'''
        config = configparser.ConfigParser()
        config.read(config_path, encoding="utf-8-sig")
        username = config.options(section)
        return username

    def get_addkey(self, user):
        '''遍历获得配置文件收件人email'''
        sum = 0
        L = []
        for i in user:
            if sum < len(user):
                emails = self.config_read('addressed', i)
                L.append(emails)
                sum += 1
        return L
