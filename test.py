# Import necessary packages
from pymeasure.instruments.keithley import Keithley2400
import logger
import varis
from time import sleep
#keithley = Keithley2400("GPIB::1")
#data = open('test.txt', mode='w')

#keithley.apply_voltage()               
#keithley.source_voltage_range = 1
#keithley.compliance_current = .1 
#keithley.source_voltage = 0        
#keithley.enable_source()       
logger.Startup(varis.kport)



logger.srcm[0].measure_current()         
logger.srcm[1].measure_current()         

logger.srcm[0].ramp_to_voltage(1)     
logger.srcm[1].ramp_to_voltage(1)     

v=logger.srcm[0].source_voltage
i=logger.srcm[1].current 
v=logger.srcm[0].source_voltage
i=logger.srcm[1].current 
r=v/i

print(logger.srcm[1].id,'''\n''','resistance=',r,'''\n''','voltage=',v,'''\n''','current=',i, file=varis.data)
print(logger.srcm[1].check_errors(), file=varis.data)
logger.srcm[1].shutdown()   
logger.srcm[0].shutdown()                                     