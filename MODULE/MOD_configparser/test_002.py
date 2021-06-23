# import configparser
#
# config = configparser.ConfigParser()
# config.read('example.ini')
#
# for key in config['DEFAULT']:
#     print(key)

import configparser
import os
config = configparser.ConfigParser()
file_path = os.path.dirname(os.path.abspath('.')) + '\MOD_configparser\example.ini'
print(file_path)

config.read(file_path)

data_1 = config.get("DEFAULT","aaa")
data_2 = config.get("DEFAULT_2","eee")
print(data_1,data_2)

