from argparse import ArgumentParser

from inspy_logger import LEVELS as LOG_LEVELS

class CMDLine(ArgumentParser):
    def __init__(self):
        super().__init__()
        
        self.description = "Return dictionary definitions to the command-line on query."
        
        self.epilog = "As seen above you can also get definitions via the GUI by passing the --gui flag when starting the program."

        log_level_grp = self.add_mutually_exclusive_group()
        log_level_grp.add_argument(
            '-v', '--verbose',
            help='Instruct the logger to output all messages to the console. (Exactly the same as passing "--log-level DEBUG"',
            action='store_true',
            required=False,
            default=False
            )
        
        log_level_grp.add_argument(
            '-l', '--log_level',
            help="Specify the level at which you'd like the logger to output messages.",
            action='store',
            choices=LOG_LEVELS,
            default='info',
        )
        
        subparsers = self.add_subparsers()
        gui_parser = subparsers.add_parser('gui')
        gui_parser.add_argument(
            '-c', '--console',
            help='Open a second GUI window that contains the console output. (Only really useful if added to a call from a desktop icon, etc.)',
            action='store_true',
            required=False,
            default=False
            )


