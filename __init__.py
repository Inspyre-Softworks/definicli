from pathlib import Path
from definicli.api import WordsAPI

started = False

class NetworkError(Exception):
    def __init__(self):
        self.message = "An unknown network error seems to have occurred"

if not started:

    APP_DIR = Path('~/Inspyre-Softworks/definicli').expanduser().resolve()
    CONF_DIR = APP_DIR.joinpath('config/')
    CACHE_DIR = Path('~/.cache/Inspyre-Softworks/definicli').expanduser().resolve()

    from definicli.tools.args_parse import ARGS

    # If we received the 'verbose' flag we log at 
    # level 'debug'
    if ARGS.verbose:
        LOG_LEVEL = 'debug'
    # Otherwise we use the value of ARGS.log_level
    else:
        LOG_LEVEL = ARGS.log_level

    from definicli.logger import ISL, ISL_DEV, start_logger, ROOT_LOG

    ROOT_LOG.debug("Stared root logger.")

    ROOT_LOG.debug(f"Argument state from command line: {ARGS}")

    from definicli.config import Settings

    SETTINGS = Settings()
    CONF = SETTINGS.Config()

    ROOT_LOG.debug(f"Config: {CONF}")

    API = WordsAPI(CONF)

    started = True
