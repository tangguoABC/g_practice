# 1、导入日志模块 import logging
# 2、取得 logging.Logger 对象--- 创建一个logger logger=logging.getLogger(“myFristlogger”)
# 3、使用 Logger 对象输出信息--- 设置logger的等级 logger.setLevel（logging.DEBUG）
# 4、创建一个handler用于写入日志文件 fh=logging.FileHander(“E/code/first.log”)
# 5、定义handler的输出格式 formatter=logging.Formatter(‘%(asctime)s-%(name)s-%(module)s-%(funcName)s-%(message)s’)
# 6、给logger添加handler logger.addHandler(fh)

import logging
# 创建一个logger
logger = logging.getLogger("my_log")
logger.setLevel(logging.INFO)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler("test.log")
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


# 记录日志

logger.debug("foobar")
logger.info("foobar2")
logging.warning("foobar3")
logging.error("foobar4")
logging.critical("foobar5")


