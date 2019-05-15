import os
import daemon

from main import main

WORKING_DIRECTORY = os.getenv('AVTYUL_BOT_WORKING_DIRECTORY')
PIDFILE = os.getenv('AVTYUL_BOT_PIDFILE')

with daemon.DaemonContext(working_directory=WORKING_DIRECTORY,
                          pidfile=PIDFILE):
    main()
