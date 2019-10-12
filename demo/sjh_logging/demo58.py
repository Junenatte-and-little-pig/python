# -*- encoding: utf-8 -*-
import logging
import getpass


class TextLoggingHandler(object):
    def __init__(self):
        self.filename = "loghandler.txt"
        self.format = logging.Formatter("%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s")
        # 获取logger对象
        self.logger = logging.getLogger(getpass.getuser())
        self.logger.setLevel(logging.INFO)
        # 输出到日志文件
        self.logging_handler = logging.FileHandler(self.filename)
        self.logging_handler.setFormatter(self.format)
        self.logging_handler.setLevel(logging.INFO)
        # 输出到控制台
        self.logging_handler_stream = logging.StreamHandler()
        self.logging_handler_stream.setFormatter(self.format)
        self.logging_handler_stream.setLevel(logging.INFO)
        # 增加handler处理
        self.logger.addHandler(self.logging_handler)
        self.logger.addHandler(self.logging_handler_stream)


textLogging = TextLoggingHandler()
textLogging.logger.critical("message")
textLogging.logger.error("message")
textLogging.logger.warning("message")
textLogging.logger.info("message")
textLogging.logger.debug("message")