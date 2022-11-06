# Import necessary packages
import logger
import varis
import vis

#startup
logger.Startup(varis.kport)

#conduct measurements
#logger.measureCVL(varis.kport,varis.ts,varis.points,varis.svr)
#logger.measureSIV(1,-1,1,50)
#capt = logger.measureRCTC(varis.kport,varis.resistance,varis.svr,varis.points,varis.Ht,varis.Lt)
#shut down
ct=logger.impedance(varis.kport,2,50,.001)
logger.shutdown(varis.kport)  

#store data   
logger.save(ct,varis.file)
#logger.save(logger.IV,varis.file)


#plot new data
#vis.cvPlot(logger.RCVL[:,0],logger.RCVL[:,3],logger.RCVL[:,6],logger.RCVL[:,1],logger.RCVL[:,4])
#vis.ivPlot(logger.IV[:,0],logger.IV[:,1])
#vis.RCPlot(capt)
vis.CTplot(ct)
