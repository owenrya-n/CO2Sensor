# Import necessary packages
from pymeasure.instruments.keithley import Keithley2400
import logger
import varis
import matplotlib.pyplot as map
from time import sleep

#collect data
logger.Startup(varis.kport)
logger.measureCVL(varis.kport,varis.ts,varis.points,varis.svr)

#shut down
logger.shutdown(varis.kport)  

#store data
#print(logger.ICVL, file=varis.data)
#print(logger.VCVL, file=varis.data)    
print(logger.RCVL, file=varis.data)
print(logger.times)

#plot saved data
map.plot(logger.RCVL[:,0],logger.RCVL[:,1])
map.plot(logger.RCVL[:,0],logger.RCVL[:,2])
map.style.use('_mpl-gallery')
map.show()

