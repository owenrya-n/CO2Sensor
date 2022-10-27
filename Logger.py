#import statements
from os import times
from pymeasure.instruments.keithley import Keithley2400
import numpy as np
from time import sleep
import varis
import pandas as pd

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
    RCVL=np.empty((pts,3*len(idet)+1), dtype=np.float)
    RCVL[:,5]=varis.svr #need to clean this up
    RCVL[:,2]=varis.svr
    RCVL[:,4]=ICVL[:,1]
    RCVL[:,1]=ICVL[:,0]
    RCVL[:,6]=np.true_divide(varis.svr,ICVL[:,1])
    RCVL[:,3]=np.true_divide(varis.svr,ICVL[:,0])#np.true_divide(varis.svr,ICVL[:,:1]) # NEED LOOP OR COPY PASte
    RCVL[:,:1]=times # DOES NOT YET SCALE WITH PORTS CONNECTED.

def save(arrayname,filename): 
    frame=pd.DataFrame(arrayname)
    if(len(arrayname[1,:]))==7:
        frame.columns=['time(s)','I1','V1','R1','I2','V2','R2']
    frame.to_csv(filename)
    print('save successful')

def measureSIV(loc,minV,maxV,pts):
    Vrange=np.arange(minV,maxV,(maxV-minV)/pts).reshape(pts,1)
    Ivals=np.zeros_like(Vrange)
    print(Vrange)
    for i in range(pts):
        srcm[loc].measure_current()
        srcm[loc].ramp_to_voltage(Vrange[i,0],2,.001)
        sleep(.01)
        Ivals[i,0]=srcm[loc].current
        sleep(.01)
        print(i)
    global IV
    IV=np.empty([pts,2])
    #IV[:,1]=times
    IV[:,0]=Vrange[:,0] #clean up this as well
    IV[:,1]=Ivals[:,0]


def shutdown(port):
    for k in range(0,len(port)):
        srcm[k].shutdown()