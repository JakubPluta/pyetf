import logging
import sys
from typing import Optional

_LOGGING_FORMATTER = (
    "[%(levelname)s] %(name)s %(processName)s:%(process)s %(threadName)s:%(thread)d"
    " %(funcName)s:%(lineno)d - %(message)s"
)

LOGGING_FORMATTER = (
    "[%(levelname)s] %(name)s %(asctime)s %(funcName)s:%(lineno)d - %(message)s"
)


logging.getLogger("urllib3").propagate = False


def get_logger(name: Optional[str] = None, level: str = "DEBUG") -> logging.Logger:
    """Returns Logger Instance with predefined formatting"""
    logger = logging.getLogger(name=name)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(LOGGING_FORMATTER)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if not level or level.upper() not in [
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ]:
        logger.warning(
            "invalid logging level: %s, setting logging level to `DEBUG`", level
        )
    logger.setLevel(level=level)
    return logger
