import sys
from .base import *

local_file = "/home/ant/Documents/Vue_app/eComVue/ecomCore/settings/__init__.py"

if __file__ == local_file:
    from .local import *
else:
    from .server import *

"""
dont forget to add BASE_DIR parent dir !! because of different settings 
"""
