import argparse
from argparse import ArgumentParser

from inspy_logger import LEVELS as LOG_LEVELS

from definicli import APP_DIR

class CMDLine(ArgumentParser):
    def __init__(self):
        p_args = dict(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        super().__init__(**p_args)

        self.description = "Return dictionary definitions to the command-line on query."
        
        self.epilog = "As seen above you can also get definitions via the GUI by passing the --gui flag when starting the program."

        self.add_argument('term', help="The word which you'd like the definition of.")
        
        _subparsers = self.add_subparsers(dest='cmds', parser_class=ArgumentParser)
        gui_parser = _subparsers.add_parser('gui', )
        gui_parser.add_argument(
            '-c', '--console',
            help='Open a second GUI window that contains the console output. (Only really useful if added to a call from a desktop icon, etc.)',
            action='store_true',
            required=False,
            default=False
            )

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

        self.add_argument('-a', '--app-dir',
                          action='store',
                          type=str,
                          required=False,
                          help="A string representing the path you'd like your application data directory to preside in.",
                          default=APP_DIR)

        self.add_argument('-A', '--API-key',
        action='store',
        help='The key for the dictionary API',
        required=False,
        default=None)


_args = CMDLine()
ARGS = _args.parse_args()
    

