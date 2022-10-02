###################################################
# Extreme Environment Microsystems Laboratory     #
# Stanford University                             #
# Owen Ryan 9-29-2022                             #
###################################################

#import statements
import pandas
import numpy
import datetime
import matplotlib.pyplot


#find resistance values (v/i=r)
def eval(current, voltage, voltagedev):
    R = numpy.divide(voltage, current)
    R_dev = numpy.divide(voltagedev, current)

def record(voltage, current, resistance, err):
    pct = numpy.divide(err, current)
    error = numpy.multiply(pct,100)
    data = pandas.DataFrame({
        'Current (A)': current,
        'Voltage (V)': voltage,
        'Resistance (Ohm)': resistance,
        'STDEV (%)' : error,
    })
    data.to_csv(datetime.datetime.now())
    print("data stored")

def plot(resistance,current,error):
    matplotlib.pyplot.plot(resistance,current)
    matplotlib.pyplot.errorbar(resistance,current,error,fmt='o')
