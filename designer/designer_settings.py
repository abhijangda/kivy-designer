import os
import shutil
import sys

from kivy.properties import ObjectProperty
from kivy.config import ConfigParser
from kivy.uix.settings import Settings, SettingTitle
from kivy.uix.label import Label
from kivy.uix.button import Button

from designer.helper_functions import get_kivy_designer_dir

DESIGNER_CONFIG_FILE_NAME = 'config.ini'

class DesignerSettings(Settings):
    '''Subclass of :class:`kivy.uix.settings.Settings` responsible for 
       showing settings of Kivy Designer.
    '''

    config_parser = ObjectProperty(None)
    '''Config Parser for this class. Instance
       of :class:`kivy.config.ConfigParser`
    '''

    def load_settings(self):
        '''This function loads project settings
        '''
        self.config_parser = ConfigParser()
        DESIGNER_CONFIG = os.path.join(get_kivy_designer_dir(),
                                       DESIGNER_CONFIG_FILE_NAME)

        if not os.path.exists(DESIGNER_CONFIG):
            shutil.copyfile(os.path.join(os.getcwd(), DESIGNER_CONFIG_FILE_NAME), DESIGNER_CONFIG)
        
        self.config_parser.read(DESIGNER_CONFIG)
        self.add_json_panel('Kivy Designer Settings', self.config_parser,
                            './designer/settings/designer_settings.json')
        
        path = self.config_parser.getdefault(
            'global', 'python_shell_path', '')
        
        if path == "":
            self.config_parser.set('global', 'python_shell_path',
                                   sys.executable)
            self.config_parser.write()
    
    def on_config_change(self, *args):
        '''This function is default handler of on_config_change event.
        '''
        self.config_parser.write()
        super(DesignerSettings, self).on_config_change(*args)