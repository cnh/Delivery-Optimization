"""
Starts a Blaze server for tests.

$ start_test_server.py /path/to/catalog_config.yaml <portnumber>
"""

from __future__ import absolute_import, division, print_function

import sys
import os

if os.name == 'nt':
    old_excepthook = sys.excepthook

    # Exclude this from our autogenerated API docs.
    undoc = lambda func: func

    @undoc
    def gui_excepthook(exctype, value, tb):
        try:
            import ctypes, traceback
            MB_ICONERROR = 0x00000010
            title = u'Error starting test Blaze server'
            msg = u''.join(traceback.format_exception(exctype, value, tb))
            ctypes.windll.user32.MessageBoxW(0, msg, title, MB_ICONERROR)
        finally:
            # Also call the old exception hook to let it do
            # its thing too.
            old_excepthook(exctype, value, tb)

    sys.excepthook = gui_excepthook

import blaze
from blaze.io.server.app import app

blaze.catalog.load_config(sys.argv[1])
app.run(port=int(sys.argv[2]), use_reloader=False)
