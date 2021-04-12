from os import makedirs
from pathlib import Path
from configparser import ConfigParser

from definicli import ISL, ISL_DEV, start_logger, ARGS, CACHE_DIR, APP_DIR

class Settings(object):
    def __init__(self, app_dir=None):
        """ Initialize a Settings object.
        
        The Settings class contains the the application's settings, as well as several sub-classes for other
        persistent configurations.
        
        Args:
            app_dir (str): Path to where you want me to place a directory to store our data in within your profile. (
            Defaults to:
        """
        cache = self.Cache()
        self.cache = cache.cache
        self.cache_fp = CACHE_DIR.joinpath('cache.ini')
        
        if app_dir is None:
            self.app_dir = APP_DIR
        else:
            self.app_dir = Path(app_dir).expanduser().resolve()
    
    
    class Config(ConfigParser):
        def __init__(self):
            super().__init__()
            self.conf_filepath = ARGS.app_dir.joinpath('conf/config.ini')

            self.log_name = 'config.Settings.Config'

            if not ISL.in_manifest(self.log_name):
                log = start_logger(self.log_name)
            else:
                log = ISL.in_manifest(self.log_name, True)

            log.debug(f"{self.log_name} initialized!")

            log.debug("Checking for app directory")

            app_dir = Path(ARGS.app_dir).expanduser()

            conf_dir = app_dir.joinpath('conf/')

            if conf_dir.exists():
                log.debug(f"Found path: {ARGS.app_dir}. Loading.")
                self.load()
            else:
                log.debug(f"Could not find path {ARGS.app_dir}. Creating.")
                makedirs(conf_dir)
                self.create()

        def load(self):
            self.read(self.conf_filepath)

            return self

        def create(self):
            """
            
            Create a config file.

            """
            conf = {
                '[DEFAULT]': {
                    'api_key': ''
                },
                '[MAIN]': {
                    'always_start_gui': False
                }
            }
            self.read_dict(conf)

            return self.write_config()

        def write_config(self):
            """
            
            Check for an existing config file at self.conf-filepath

            """
            conf_dest = self.conf_filepath

            with open(conf_dest, 'w') as fp:
                self.write(fp)

            return self.load
        
    
    
    class Cache(object):
        
        class AlreadyLoadedError(Exception):
            def __init__(self):
                """
                
                Raised when a cache is already loaded in this instance.
                
                Note:
                    If you receive this error it might be beneficial to try:
                    ```python
                      >>> <cache_obj>.reload()
                    ```
                    Be aware that this will delete any file that matches upon call.
                
                """
                msg = "The cache is already loaded. If you want to reload it from disk try .reload"
                self.message = msg
                self.msg = msg
        
        
        def check(self):
            """ Check to see if the cachefile exists
            
            Checks the filesystem for the cachefile at '~/.cache/Inspyre-Softworks/definicli/cache.ini'
            
            Returns:
                False (bool): Returned when there's no file at the location
                True (bool): Returned when there is a file that seems properly formatted

            """
            if self.cache:
                raise Settings.Cache.AlreadyLoadedError()
            if self.fp.exists() and self.fp.is_file():
                return True
            else:
                return False
        
        def create(self):
            """ Creates a new cache
            
            Creates a new ConfigParser object that only has a 'DEFAULT' section.
            
            
            Returns:

            """
            
            _ = {
                    'DEFAULT': {
                            'app_dir': self.app_fp
                            }
                    }
            parser = ConfigParser()
            parser.read_dict(_)
            self.cache = parser
            
            makedirs(self.fp)
            self.write()
            
            return self.load()
        
        def load(self):
            if self.cache:
                raise Settings.Cache.AlreadyLoadedError()
            else:
                parser = ConfigParser()
                parser.read(self.fp)
                self.cache = parser
                
                self.loaded = True
                
                return parser
        
        def reload(self):
            """
            
            Reload the cachefile from disk.
            
            Returns:
                parser (ConfigParser): A ConfigParser object with the path to the actual config file.

            """
            self.cache = None
            
            return self.load()
        
        def write(self):
            with open(self.fp, 'w') as fp:
                self.cache.write(fp)
        
        def __init__(self, reload_if_exists=False):
            
            self.log_name = 'definicli.Settings.Cache'

            if not ISL.in_manifest(self.log_name):
                log = start_logger(self.log_name)
            else:
                log = ISL.in_manifest(self.log_name, True)
            
            debug = log.debug
            self.fp = Path('~/.cache/Inspyre-Softworks/definicli/cache.ini').expanduser()
            self.app_fp = ARGS.app_dir
            
            self.app_fp = Path('~/Inspyre-Softworks/definicli/config/config.ini').expanduser()
            
            debug(f"Cache filepath: {self.fp}")
            debug(f"Default app directory: {self.app_fp}")
            
            debug("Setting tracking variables")
            self.loaded = False
            debug(f"var | .loaded = False")
            self.cache = None
            debug(f"var | .cache == None")
            
            debug(f'Checking for existing cachefile...')
            
            try:
                if self.check:
                    debug(f"Found a cache file at {self.fp}")
                    self.load()
                else:
                    self.create()
            except Settings.Cache.AlreadyLoadedError as e:
                print(e.msg)
                if reload_if_exists:
                    self.reload()
                else:
                    print("Try '.reload' or try to initialize the cache again with the parameter 'reload_if_exists' set as bool(True)")
                    raise
