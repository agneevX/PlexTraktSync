import logging

from .factory import factory


def initialize():
    CONFIG = factory.config()
    # global log level for all messages
    log_level = logging.DEBUG if CONFIG.log_debug else logging.INFO

    # messages with info and above are printed to stdout
    console_handler = factory.console_logger()
    console_handler.terminator = ""
    console_handler.setFormatter(logging.Formatter("%(message)s"))
    console_handler.setLevel(logging.INFO)

    # file handler can log down to debug messages
    mode = "a" if CONFIG["logging"]["append"] else "w"
    file_handler = logging.FileHandler(CONFIG.log_file, mode, "utf-8")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)-15s %(levelname)s[%(name)s]:%(message)s")
    )
    file_handler.setLevel(logging.DEBUG)

    handlers = [
        file_handler,
        console_handler,
    ]
    logging.basicConfig(handlers=handlers, level=log_level)

    # Set debug for other components as well
    if log_level == logging.DEBUG:
        from plexapi import log as logger
        from plexapi import loghandler

        logger.removeHandler(loghandler)
        logger.setLevel(logging.DEBUG)


initialize()
logger = logging.getLogger("PlexTraktSync")
