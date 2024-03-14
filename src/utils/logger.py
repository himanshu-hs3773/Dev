"""
Import:
from src.utils.logger import info, warning, error, critical #noqa: F401 pylint: disable=W0611

Usage:
    info("InfoMsg", logDetail="Info details")
    info("InfoMsgWithMetadata[%s]", "metadataStr", logDetail="Info details")
    warning("WarnMsg", logDetail="Warning details")
    error("ErrorMsg", logDetail="Error details")
    critical("criticalMsg", logDetail="Error details")

Logs to directory and file:
LOCAL: ./.log/‹filename>.log
LOG_DIR_PATH: --
"""

import inspect
import logging
import os
import sys
from datetime import datetime
from typing import Dict, Tuple

import json_logging
from json_log_formatter import JSONFormatter

from collections.abc import Callable

ys: str = "\033[0;93m"
yw: str = "\033[0;33m"
rw: str = "\033[0;31m"
rwb: str = "\033[0;1;31m"
rsb: str = "\033[1;91m"
wsl: str = "\033[0;2;97m"
ws: str = "\033[0;97m"
wwb: str = "\033[0;1;39m"
wwbl: str = "\033[1;2;39m"
cs: str = "\033[0;96m"
e_: str = "\033[0m"


def singleton(class_) -> Callable:
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance()


class StreamFormatter(logging.Formatter):
    def __init__(self) -> None:
        super().__init__()
        # module = str(os-path. basename (sys.argv[01)). replace("-py", "'*)
        # fmt = f"%(levelname)s{wsl}:: (module}:: {cs}%(message)s"
        fmt = f"%(levelname)s{wsl}:: {cs}%(message)s"
        self.FORMATS: Dict[int, str] = {
            logging.DEBUG: f"{wwbl}{fmt}{e_}",
            logging.INFO: f"{wwb}{fmt}{e_}",
            logging.WARNING: f"{ys}{fmt}{e_}",
            logging.ERROR: f"{rwb}{fmt}{e_}",
            logging.CRITICAL: f"{rsb}{fmt}{e_}",
        }

    def format(self, record) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class Logger:
    _instance = None

    def __new__(cls, logfile=None):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            # initialization
            cls.file_logger = cls.get_file_logger(logfile)
            cls.stream_logger = cls.get_stream_logger()
        return cls._instance

    @staticmethod
    def get_file_logger(logfile) -> logging.Logger:
        """Create logger object.

        :rtype:: logging.Logger
        returns: Logger
        """
        json_logging.init_non_web()
        json_logging.ENABLE_JSON_LOGGING = False
        logger = logging.getLogger("file_logger")
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(filename=logfile)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(JSONFormatter())
        logger.addHandler(file_handler)
        return logger

    @staticmethod
    def get_stream_logger() -> logging.Logger:
        """Create logger object.
        rtype: logging. Logger
        returns: Logger
        """
        logger = logging.getLogger("stream_logger")
        logger.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(StreamFormatter())
        logger.addHandler(stream_handler)
        return logger

    @staticmethod
    def compile(msg: str, args: tuple, kwargs: dict) -> Tuple[str, dict, str]:
        if args:
            msg = msg % str(*args)
        kwargs["logTime"] = datetime.now().strftime("%m.%d.%Y %H:%M")
        kwargs["logType"] = os.path.basename(sys.argv[0])
        file, line, method = inspect.stack()[2][1:4]
        splitter = "/"
        if "\\" in str(file):
            splitter = "\\"
        caller = f"{str(file).split(splitter)[-1][:-3]}::{method}::{line}::"
        kwargs["loggedFrom"] = caller[:-2]
        return msg, kwargs, caller

    def info(self, msg, *args, **kwargs) -> None:
        msg, extras, caller = self.compile(msg, args, kwargs)
        self.file_logger.info(msg, extra=extras)
        self.stream_logger.info("%s%s%s%s", wsl, caller, cs, msg)

    def warning(self, msg, *args, **kwargs) -> None:
        msg, extras, caller = self.compile(msg, args, kwargs)
        self.file_logger.warning(msg, extra=extras)
        self.stream_logger.warning("%s%s%s%s", wsl, caller, cs, msg)
        if "logDetail" in kwargs:
            sys.stderr.write(f">> {yw}{kwargs.get('error') or kwargs['logDetail']}{e_}\n")

    def error(self, msg, *args, **kwargs) -> None:
        msg, extras, caller = self.compile(msg, args, kwargs)
        self.file_logger.error(msg, extra=extras)
        self.stream_logger.error("%s%s%s%s", wsl, caller, cs, msg)
        if "logDetail" in kwargs:
            sys.stderr.write(f">> {rw}{kwargs.get('error') or kwargs['logDetail']}{e_}\n")

    def critical(self, msg, *args, **kwargs) -> None:
        msg, extras, caller = self.compile(msg, args, kwargs)
        self.file_logger.critical(msg, extra=extras)
        self.stream_logger.critical("%s%s%s%s", wsl, caller, cs, msg)
        if "logDetail" in kwargs:
            sys.stderr.write(f">> {rwb}{kwargs.get('error') or kwargs['logDetail']}{e_}\n")


if __name__ == "src.utils.logger":
    log_dir = os.getenv("LOG_PATH")
    if not log_dir:
        log_dir = f"{os.getcwd()}\\.log"
    f_name = str(os.path.basename(sys.argv[0])).replace(".py", ".log")
    log_file = f"{log_dir}\\{f_name}"

    if not os.path.isdir(log_dir):
        os.mkdir(log_dir, mode=0o777, dir_fd=None)
    logger_instance = Logger(logfile=log_file)
    info = logger_instance.info
    warning = logger_instance.warning
    error = logger_instance.error
    critical = logger_instance.critical
