import configparser
import os


class TestReadConfigFile(object):

    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))  # 获取项目根目录的相对路径
        print( root_dir)

        config = configparser.ConfigParser()

        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        url = config.get("testServer", "URL")

        return (browser, url)  # 返回的是一个元组


trcf = TestReadConfigFile()
print (trcf.get_value())
"""
在配置文件一般#表示注释，你想要哪行配置代码起作用，
你就把前面的#去除，并且在注释其他同一个区域。在ini
文件中 中括号包裹起来的部分叫section，了解一下就可以。
"""