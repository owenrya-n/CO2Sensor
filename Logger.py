#import statements
from os import times
from pymeasure.instruments.keithley import Keithley2400
import numpy as np
from time import sleep
import varis

#connect to Sourcemeter
def Startup(port): #use arrays
    global srcm
    srcm = [None] * len(port)
    for k in range(0,len(port)):
        srcm[k] = Keithley2400(port[k])
        ID = srcm[k].id
        srcm[k].reset()
        srcm[k].use_front_terminals()
        srcm[k].apply_voltage()
        srcm[k].source_voltage_range=varis.svr
        srcm[k].compliance_current=varis.comc
        srcm[k].enable_source()
    print("CV Front Terminals Configured")


def measureCVL(idet,timestep,pts,voltage):
    time = np.linspace(0,timestep*pts,pts)
    global times
    times = np.reshape(time, (pts,1))

    for k in range(0,len(idet)):
        srcm[k].measure_current()
        srcm[k].ramp_to_voltage(voltage)
    global ICVL
    ICVL=np.empty((pts,len(idet)), dtype=np.float)
    global VCVL
    VCVL=np.empty_like(ICVL)
    print('start')
    for j in range(pts):
        for f in range(0,len(idet)):
            ICVL[j,f] = srcm[f].current
            VCVL[j,f] = srcm[f].source_voltage
        sleep(timestep)   
    global RCVL
    RCVL=np.empty((pts,len(idet)+1), dtype=np.float)
    RCVL[:,2]=np.true_divide(varis.svr,ICVL[:,1])
    RCVL[:,1]=np.true_divide(varis.svr,ICVL[:,0])#np.true_divide(varis.svr,ICVL[:,:1]) # NEED LOOP OR COPY PASte
    RCVL[:,:1]=times # DOES NOT YET SCALE WITH PORTS CONNECTED.
def shutdown(port):
    for k in range(0,len(port)):
        srcm[k].shutdown()
