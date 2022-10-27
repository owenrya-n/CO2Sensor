#import statements
import matplotlib.pyplot as map
def cvPlot(time,r1,r2,i1,i2):
    fig, (r,c) = map.subplots(1,2)
    map.suptitle('Resistance and Current with Respect to time')
    r.plot(time,r1)
    r.plot(time,r2)
    r.set(xlabel='t (ms)',ylabel='resistance (ohms)')

    c.loglog(time,i1)
    c.loglog(time,i2)
    c.set(xlabel='t (ms)',ylabel='current (amps)')
    map.show()

def ivPlot(imtx,vmtx):
    map.suptitle('IV Plot')
    map.plot(imtx,vmtx)
    #map.set(xlabel='voltage(volts)',ylabel='current(amps)')
    map.show()