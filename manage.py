# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 18:03:42 2018

@author: Camille
"""

#!/usr/bin/env python

from src import create_app
from flask_script import Manager
from flask_script import Server

app = create_app()
manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True, host='0.0.0.0'))

if __name__ == '__main__':
    manager.run()