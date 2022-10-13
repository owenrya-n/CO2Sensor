# Import necessary packages
from pymeasure.instruments.keithley import Keithley2400
import logger
import varis
from time import sleep

#collect data
logger.Startup(varis.kport)
logger.measureCVL(varis.kport,varis.ts,varis.points,varis.svr)

#shut down
logger.shutdown(varis.kport)  

#store data
print(logger.ICVL, file=varis.data)
print(logger.VCVL, file=varis.data)    
                          
