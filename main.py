import PySimpleGUI as gui
from definicli.config import Settings

settings = Settings()
config = settings.Config()

print(config.sections())

