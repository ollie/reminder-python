#!/usr/bin/env python3

import sys, codecs

# Needed for NerdTool
sys.stdout = codecs.getwriter('utf-8')( sys.stdout.detach() )

from app.boot import App

app = App()
app.run()
