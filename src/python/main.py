import os
os.system("clear")

######################
#### python setup ####
######################

from functions.helper.libraries import install_libraries, check_requirements

install_libraries(check_requirements("src/python/requirements.txt"))

#########################
#### install mongodb ####
#########################

from functions.mongodb.mongodb import install_mongodb
install_mongodb()