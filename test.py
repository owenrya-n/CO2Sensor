# Import necessary packages
from multiprocessing import current_process
from pymeasure.instruments.keithley import Keithley2400
import numpy as np
import pandas as pd
from time import sleep
keithley = Keithley2400("GPIB::1")
data = open('test.txt', mode='w')

keithley.apply_voltage()               
keithley.source_voltage_range = 1
keithley.compliance_current = .1 
keithley.source_voltage = 0        
keithley.enable_source()          

keithley.measure_current()         

keithley.ramp_to_voltage(1)     
v=keithley.source_voltage
i=keithley.current 
r=v/i

print(keithley.id,'''\n''','resistance=',r,'''\n''','voltage=',v,'''\n''','current=',i, file=data)
print(keithley.check_errors(), file=data)
keithley.shutdown()                    