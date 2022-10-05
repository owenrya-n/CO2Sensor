#import statements
from pymeasure.instruments.keithley import Keithley2400
import numpy
from time import sleep
import vars



#connect to Sourcemeter
def Startup():
    global Sourcemeter 
    Sourcemeter = Keithley2400(vars.kport)
    Sourcemeter.id
    Sourcemeter.reset()
    Sourcemeter.use_front_terminals()
    Sourcemeter.measure_voltage()
    Sourcemeter.config_current_source()
    sleep(vars.delay) 
    Sourcemeter.set_buffer(vars.avgs)
    print("connected to Keithley2400 Sourcemeter")

def alloc(Imin, Imax, Res, CC, Resolution):
    global I
    I = numpy.linspace(Imin, Imax, Res) #ramp current 
    global I2
    I2 = numpy.zeros(Resolution)+CC #constant current 
    global V2 
    V2 = numpy.zeros_like(I2)
    global V
    V = numpy.zeros_like(I)
    global V_dev 
    V_dev = numpy.zeros_like(I)
    global R
    R = numpy.zeros_like(I)
    global R_dev
    R_dev = numpy.zeros_like(I)
    print("allocation successful")
    print("memory allocated")

def measure(MRes):
    for k in range(MRes):
        Sourcemeter.current = I[k]
        Sourcemeter.reset_buffer()
        sleep(vars.delay)
        Sourcemeter.start_buffer()
        Sourcemeter.wait_for_buffer()
        V[k] = Sourcemeter.means
        V_dev[k] = Sourcemeter.standard_devs
    print("success")

def measureCC(timestep,Resolution):
    for j in range(Resolution):
        Sourcemeter.current = I2[j]
        V2[j] = Sourcemeter.measure_voltage
        sleep(timestep)
    
def shutdown():
    Sourcemeter.shutdown()
    del I; del V; del V_dev; del R; del R_dev
    print("shutdown")
