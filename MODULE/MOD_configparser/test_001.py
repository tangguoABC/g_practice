import configparser
"""
用configparser类来生成这样一个配置文件

"""
config  = configparser.ConfigParser()
# 第一种方式
config['DEFAULT'] = {
    'aaa' : '111',
    'bbb' : '222',
    'ccc' : '333'
}
# 第二种方式
config['DEFAULT_2'] = {}
config['DEFAULT_2']['eee'] = '888'

with open('example.ini','w') as configfile:
    config.write(configfile)

