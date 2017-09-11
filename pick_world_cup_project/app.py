#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plugins import app
from plugins.users.views import *
from plugins.bets.views import *
from plugins.competitions.views import *


if __name__ == '__main__':
    app.run()
