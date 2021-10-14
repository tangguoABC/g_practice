# import configparser
#
# config = configparser.ConfigParser()
# config.read('example.ini')
#
# for key in config['DEFAULT']:
#     print(key)

import configparser
import os
config = configparser.ConfigParser()  # 初始化实例，
file_path = os.path.dirname(os.path.abspath('.')) + '\MOD_configparser\example.ini'

config.read(file_path, encoding="utf-8") # 读取配置文件

data_1 = config.get("DEFAULT","aaa")
data_2 = config.get("DEFAULT_2","eee")
print(data_1,data_2)

