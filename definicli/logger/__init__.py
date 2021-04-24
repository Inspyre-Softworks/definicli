# ****** is_home_hub/logger/__init__.py ****** #
# Description: A sub-package init for managing
#              logger.
# Time of Creation: 4/4/21 at 4:56 PM
# Author: Taylor-Jayde J. Blackstone <t.blackstone@inspyre.tech>
# ************************ #
from inspy_logger import InspyLogger

LOG_LEVEL = 'info'


class ISL(InspyLogger):
    def __init__(self):
        super().__init__()
        
        self.Device = self.LogDevice("definicli", LOG_LEVEL)
        
        if not self.Device.started:
            self.rt_logger = self.Device.start()
        else:
            pass
    
    def in_manifest(self, name, return_log_on_true=False):
        """
        
        Check to see if the given name exists in the logger manifest.
        
        Args:
            name                (str): The name of the logger you're looking for in the InspyLogger.LogDevice manifest.
            return_log_on_true (bool): Should I return the stored log device instead of bool(True) if we find it?
                                           - True: Return log device instead of bool(True) to the caller
                                           - False: Just return True if we find the given name in the logger manifest.
    
        Returns:
            True  (bool): The provided name was found in the manifest.
            False (bool): The provided name was **not** found in the manifest.
    
        """
        manifest = self.Device.manifest
        for entry in manifest:
            if entry['child_name'] == name:
                if return_log_on_true:
                    return entry['log_device']
                else:
                    return True
            else:
                return False


isl = ISL()
ISL_DEV = isl.Device
ROOT_LOG = isl.rt_logger
ISL = isl

def chg_lvl(lvl):
    ISL_DEV.adjust_level(lvl, True)

def start_logger(name):
    global isl
    """
    
    Args:
        name:

    Returns:

    """
    if isl.in_manifest(name=name):
        log = isl.in_manifest(name, return_log_on_true=True)
    else:
        log = ISL_DEV.add_child(name)
        log.debug(f"Logger started for {log.name}")
    
    return log
