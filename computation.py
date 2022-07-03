from __GLOBALS__ import RETURN_DICT as RETURN_DICT
from __GLOBALS__ import THREADS as THREADS
from __GLOBALS__ import PATH as PATH

from threading import Thread
import time

class ServerSideComputation(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        self.start_timer()

    def start_timer(self):
        while True:
            
            time.sleep(60)
