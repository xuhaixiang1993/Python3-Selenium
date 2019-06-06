from Common.config import Config


section = 'selenium'
username = '测试'
password = '一下'

test = Config()

test.config_write(section)
test.config_write(section, 'username', username)
test.config_write(section, 'password', password)

get_username = test.config_read(section, 'username')
get_password = test.config_read(section, 'password')

test.config_delete(section, 'usrename', )
test.config_delete(section, 'password')
test.config_delete(section)