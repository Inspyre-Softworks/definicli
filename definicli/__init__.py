from pathlib import Path


started = False

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

    from definicli.logger import ROOT_LOG, chg_lvl, ISL, ISL_DEV, start_logger

    if not ROOT_LOG.level == LOG_LEVEL:
        chg_lvl(LOG_LEVEL)

    ROOT_LOG.debug("Stared root logger.")

    ROOT_LOG.debug(f"Argument state from command line: {ARGS}")

    from definicli.config import Settings

    SETTINGS = Settings()
    CONF = SETTINGS.Config()

    ROOT_LOG.debug(f"Config: {CONF}")

    from definicli.tools.prompts import attention, get_input

    if ARGS.API_key:
        CONF['MAIN']['api_key'] = ARGS.API_key
        CONF.write_config()

    if CONF['MAIN']['api_key'] == '':
        cont = attention("An API key is required use DefInICLI!", "API Key Needed")

        if cont:
            api_key = get_input("Please provide an API key:", title="Enter API Key")
            if len(api_key) >= 10:
                CONF['MAIN']['api_key'] = api_key
                CONF.write_config()
        else:
            exit(1)

    api_key = CONF['MAIN']['api_key']

    from definicli.api import API, lookup_word, clean_response
    
    API.authenticate(CONF['MAIN']['api_key'])

    res = lookup_word(ARGS.term)

    lines = clean_response(ARGS.term, res)

    counter = 0

    for line in lines:
        counter += 1
        print()
        print(f"{counter} | {line}")

    started = True
