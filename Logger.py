###################################################
# Extreme Environment Microsystems Laboratory     #
# Stanford University                             #
# Owen Ryan 9-29-2022                             #
###################################################

#import statements
from turtle import Vec2D
import Vars
from pymeasure.instruments.keithley import Keithley2400
import numpy
from time import sleep


#connect to sourcemeter
def startup():
    global sourcemeter 
    sourcemeter = Keithley2400(Vars.kport)
    sourcemeter.id
    sourcemeter.reset()
    sourcemeter.use_front_terminals()
    sourcemeter.measure_voltage()
    sourcemeter.config_current_source()
    sleep(Vars.delay) 
    sourcemeter.set_buffer(Vars.avgs)
    print("connected to Keithley2400 sourcemeter")

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
        sourcemeter.current = I[k]
        sourcemeter.reset_buffer()
        sleep(Vars.delay)
        sourcemeter.start_buffer()
        sourcemeter.wait_for_buffer()
        V[k] = sourcemeter.means
        V_dev[k] = sourcemeter.standard_devs
    print("success")

def measureCC(timestep,Resolution):
    for j in range(Resolution):
        sourcemeter.current = I2[j]
        V2[j] = sourcemeter.measure_voltage
        sleep(timestep)
    
def shutdown():
    sourcemeter.shutdown()
    del I; del V; del V_dev; del R; del R_dev
    print("shutdown")
