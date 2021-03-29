from os import makedirs
from pathlib import Path
from configparser import ConfigParser
import inspy_logger
from inspy_logger import getLogger, InspyLogger

APP_DIR = Path('~/Inspyre-Softworks/definicli').expanduser().resolve()
CONF_DIR = APP_DIR.joinpath('config/')
CACHE_DIR = Path('~/.cache/Inspyre-Softworks/definicli').expanduser().resolve()


class Settings(object):
    def __init__(self, app_dir=None):
        """ Initialize a Settings object.
        
        The Settings class contains the the application's settings, as well as several sub-classes for other
        persistent configurations.
        
        Args:
            app_dir (str): Path to where you want me to place a directory to store our data in within your profile. (
            Defaults to:
        """
        self.cache = self.Cache()
        self.cache_fp = CACHE_DIR.joinpath('cache.ini')
        
        if app_dir is None:
            self.app_dir = APP_DIR
        else:
            self.app_dir = Path(app_dir).expanduser().resolve()
    
    
    class Config(ConfigParser):
        def __init__(self):
            self.conf_filepath = APP_DIR.joinpath()

        def load(self):
            """ 
            
            Load the config-file 

            """
            pass

        def create(self):
            """
            
            Create a config file.

            """
            pass

        def check(self):
            """
            
            Check for an existing config file at self.conf-filepath

            """
        
    
    
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
        
        def __init__(self, parsed_args, reload_if_exists=False):
            
            self.log_name = 'definicli.Settings.Cache'
            log = getLogger(self.log_name)
            
            debug = log.debug
            self.fp = Path('~/.cache/Inspyre-Softworks/definicli/cache.ini').expanduser()
            self.app_fp = parsed_args.app_dir
            
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
