"""
- The main header for all objects
- Usable for any object
"""

from plibs import os, sys, platform, psutil, QApplication, QTranslator


# OS info
OS_TYPE = platform.system().lower()
ARCH_TYPE = platform.architecture()[0]
IS_WINDOWS = (OS_TYPE == 'windows')
IS_LINUX = (OS_TYPE == 'linux')
IS_MAC = (OS_TYPE == 'darwin')


# Application info
SOFTWARE_NAME = 'Payroma'
VERSION = 'Decentralize Wallet v2.2021-11'
SECRET_VALUE = (
    # Set the application password here, EX: test = (116, 101, 115, 116)
    (116, 101, 115, 116)
)


# Websites
class Website:
    PAYROMA = 'www.payroma.com'


# Directories
class Dir:
    if IS_WINDOWS:
        DESKTOP = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    else:
        DESKTOP = os.path.join(os.environ['HOME'], 'Desktop')
    LANGUAGES = 'languages'
    SETTINGS = 'settings'
    DATABASE = 'database'
    TEMP = 'temp'
    LOGS = 'logs'


# Settings Options  // Set settings options here
class SettingsOption:
    pass


# Shortcuts
class Global:
    processExecutable = psutil.Process()
    kernel = QApplication(sys.argv)
    translator = QTranslator()
    logsSystem = None
    settings = None
