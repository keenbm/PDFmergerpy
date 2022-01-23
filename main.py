import logging
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='w')
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

logging.info("Calling GUICode file ")
from GUI import GUICode
logging.info("Returned from file ")

#!/usr/bin/python
from subprocess import Popen
import sys
import time

#filename = 'GUI/GUICode.py'
#p = Popen("python " + filename, shell=True)
#while True:
 #   print("\nStarting " + filename)
  #  p = Popen("python " + filename, shell=True)
   # time.sleep(3600)
    #Popen.terminate(p)
    #p.wait()
