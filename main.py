from __GLOBALS__ import RETURN_DICT as RETURN_DICT
from __GLOBALS__ import THREADS as THREADS
from __GLOBALS__ import PATH as PATH
from __GLOBALS__ import APP as app

import computation
import layout_manager

import sys
sys.path.append(PATH)

if __name__  == "__main__":
    computation_thread = computation.ServerSideComputation()
    computation_thread.start()

    app.title = "Employ Konrad"
    app.run_server(host  = '192.168.68.101') 