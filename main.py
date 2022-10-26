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
print(logger.RCVL, file=varis.data)
print(logger.times)

#plot new data
fig, (r,c) = map.subplots(1,2)
map.suptitle('Resistance and Current with Respect to time')
r.plot(logger.RCVL[:,0],logger.RCVL[:,3])
r.plot(logger.RCVL[:,0],logger.RCVL[:,6])
r.set(xlabel='t (ms)',ylabel='resistance (ohms)')

c.loglog(logger.RCVL[:,0],logger.RCVL[:,1])
c.loglog(logger.RCVL[:,0],logger.RCVL[:,4])
c.set(xlabel='t (ms)',ylabel='current (amps)')



map.show()

