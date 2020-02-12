import sys


# Pull in the local changes.
try:
    from demoDjango2.settings_module.local_settings import *
except ImportError:
    print('''
    copy
        <root>/demoDjango2/settings_module/local_settings.example.py
    into
        <root>/demoDjango2/settings_module/local_settings.py
    ''')
    sys.exit()
