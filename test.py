import matplotlib.pyplot as map
import Logger
map.plot(logger.RCVL[:,0],logger.RCVL[:,1])
map.plot(logger.RCVL[:,0],logger.RCVL[:,2])
map.style.use('_mpl-gallery')
map.show()
