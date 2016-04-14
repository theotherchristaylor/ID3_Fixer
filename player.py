
# player.py
# Class to play and stop mp3 files in a subprocess
#
# Written by Chris Taylor, 3/25/16
import sys
import os
import subprocess
import time
import signal

class Player:
            
        def __init__(self):
            self.process = subprocess
        
        def play(self, track):
            executeLine = "mpg123 -k 2500 \"" + track + "\""
            self.process = subprocess.Popen(executeLine, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        def stop(self):
            os.killpg(self.process.pid, signal.SIGTERM)
