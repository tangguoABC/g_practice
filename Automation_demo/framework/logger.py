import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 再创建一个handler，用于写入日志文件
        current_file = os.listdir(os.getcwd())
        if 'Logs' in current_file:
            pass
        else:
            os.mkdir('Logs')
        moment = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.getcwd() + '\\Logs\\'
        log_name = log_path + moment + '.log'
        print(log_name)

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def getlog(self):
        return self.logger