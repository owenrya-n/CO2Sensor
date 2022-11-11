#import statements
from os import times
from pymeasure.instruments.keithley import Keithley2400
import numpy as np
from time import sleep
import varis
import pandas as pd

#connect to Sourcemeter
def Startup(port): 
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
    RCVL[:,:1]=times
    for k in range(0,len(idet)):    #EXPERIMENTAL 
        RCVL[:,3*k+2]=varis.svr     #TRUE CODE IS COMMENTED OUT
        RCVL[:,3*k+1]=ICVL[:,k]     #NEED TO HANDLE BUGS
        RCVL[:,3*k+3]=np.true_divide(varis.svr,ICVL[:,k])
    #RCVL[:,4]=ICVL[:,1]
    #RCVL[:,5]=varis.svr
    #RCVL[:,6]=np.true_divide(varis.svr,ICVL[:,1])

def save(arrayname,filename): 
    frame=pd.DataFrame(arrayname)
    #if(len(arrayname[0,:]))==7:
    #    frame.columns=['time(s)','I1','V1','R1','I2','V2','R2']
    frame.to_csv(filename)
    print('Save Successful')

def measureSIV(loc,minV,maxV,pts): #deprecated
    Vrange=np.arange(minV,maxV,(maxV-minV)/pts).reshape(pts,1)
    Ivals=np.zeros_like(Vrange)
    for i in range(pts):
        srcm[loc].measure_current()
        srcm[loc].ramp_to_voltage(Vrange[i,0],2,.001)
        sleep(.01)
        Ivals[i,0]=srcm[loc].current
        sleep(.01)
        print(i)
    global IV
    IV=np.empty([pts,2])
    IV[:,0]=Vrange[:,0] 
    IV[:,1]=Ivals[:,0]
    print('IV Profile Generated')

def measureRCTC(idet,resistance,Vin,pts,Htime,Ltime):
    #global HVoltages
    #global LVoltages
    #global Distimes
    #global Capacitances
    totals = np.zeros(((len(idet)+1),pts))
    HVoltages = np.zeros((len(idet),pts))
    LVoltages = np.zeros((len(idet),pts))
    Distimes = np.zeros((1,pts))+Ltime
    Capacitances = np.zeros((len(idet),pts))
    for k in range(0,len(idet)):
        srcm[0].measure_voltage()
    for j in range(0,pts): #this is bad I need to fix it
        for l in range(0,len(idet)):
            srcm[l].output_off_state='ZERO'
            srcm[l].ramp_to_voltage(Vin,2,.01)#,1,0.1)#can I set this to 0.0?
            sleep(Htime) #set this to something appropriate
            HVoltages[l,j]=srcm[l].voltage
            #srcm[k].compliance_current=.001
            srcm[l].disable_source()#srcm[l].ramp_to_voltage(0,2,.01)#can I set this to 0.0?
            sleep(Ltime)
            LVoltages[l,j]=srcm[l].voltage
            srcm[l].enable_source()#sleep(Ltime) #set this to something appropriate
            print(HVoltages[l,j])
            print(LVoltages[l,j])
            #srcm[k].compliance_current=varis.comc
            srcm[l].enable_source()
            
            #srcm[l].output_off_state='ZERO'
            #srcm[l].enable_source()
            
        #for n in range(0,len(idet)): #definitely need to restructure this
            
            
    Capacitances = np.transpose(np.reciprocal(np.log(np.divide(HVoltages,LVoltages)))*(-1)*Ltime/resistance)
    timeC= np.transpose(np.reciprocal(np.log(np.divide(HVoltages,LVoltages))))
    #totals[:1,:]=Distimes
    #for q in range(0,len(idet)):
    #    totals[:,q+1]=Capacitances[:,q]
    #return totals
    #return np.transpose(LVoltages)
    return np.transpose(LVoltages)
    
def shutdown(port):
    for k in range(0,len(port)):
        srcm[k].shutdown()

def impedance(idet,Vmax,period,duration,timestep):
    for k in range(0,len(idet)):
        # Loop through each current point, measure and record the voltage
        sleep(0.1)
        srcm[k].measure_current()
        points=int(duration/timestep)

        tloc=np.linspace(0,duration,points)
        phase=np.sin(2*np.pi*tloc/period)
        #phase=np.sin(np.linspace(0,5*np.pi,pts))
        currents=np.zeros_like(phase)
        output=np.zeros([3,points])
        voltage=np.zeros_like(phase)
        print(tloc/period)
        print(phase)
        voltage=Vmax+Vmax*phase
        
        for i in range(points):
            
            srcm[k].source_voltage = voltage[i]
            currents[i] = srcm[k].current
            #sleep(.01)
            #srcm[k].reset_buffer()
            #srcm[k].wait_for_buffer()
            
            #srcm[k].stop_buffer()

    #capacitances=np.divide(currents/0.0001,(Vmax/(pts*timestep)))
    output[0,:]=tloc
    output[1,:]=voltage-Vmax
    output[2,:]=currents
    return output


        


