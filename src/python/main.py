import sys
sys.dont_write_bytecode = True

import os
os.system("clear")

######################
#### python setup ####
######################

from functions.helper.libraries import install_libraries, check_requirements

install_libraries(check_requirements("src/python/requirements.txt"))

############################
#### connect to mongodb ####
############################

from functions.mongodb.mongodb import mdb_connect

conn = mdb_connect()

