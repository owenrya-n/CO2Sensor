#Current setup characterizes resistance at varying currents


#import statements
import Logger
import Vis
import Vars

#initialization
Logger.startup
Logger.alloc(Vars.minI, Vars.maxI, Vars.data_points, Vars.Constant_Current, Vars.data_points_2)


#record data
Logger.measure(Vars.data_points)
Vis.eval(Logger.I,Logger.V,Logger.V_dev)
Vis.record(Logger.V,Logger.I,Logger.R,Logger.R_dev)

#plot
Vis.plot(Logger.R,Logger.I,Logger.R_dev)
#shutdown
Logger.shutdown