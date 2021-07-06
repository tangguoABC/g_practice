import logging
# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.INFO)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)
# 记录一条日志
logger.info('foorbar')
logger.debug("foobar")    # 不输出
logger.info("foobar")        # 输出
logger.warning("foobar")  # 输出
logger.error("foobar")      # 输出
logger.critical("foobar")    # 输出
