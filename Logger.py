#import statements
from pymeasure.instruments.keithley import Keithley2400
import numpy as np
from time import sleep
import varis

#connect to Sourcemeter
def Startup(port): #use arrays
    global srcm
    srcm = [None] * len(port)
    for k in range(0,2):
        srcm[k] = Keithley2400(port[k])
        ID = srcm[k].id
        srcm[k].reset()
        srcm[k].use_front_terminals()
        srcm[k].apply_voltage()
        srcm[k].source_voltage_range=varis.svr
        srcm[k].compliance_current=varis.comc
        srcm[k].enable_source()
    print("CV Front Terminals Configured")

def alloc(pts):
    global Vsource
    Vsource=np.zeros(pts)
    print("allocation successful")
    print("memory allocated")


def measureCVL(idet,timestep,Resolution):
    for j in range(Resolution):
        srcm[idet].current = I2[j]
        V2[j] = Sourcemeter.measure_voltage
        sleep(timestep)
    
def shutdown():
    Sourcemeter.shutdown()
    del I; del V; del V_dev; del R; del R_dev
    print("shutdown")
