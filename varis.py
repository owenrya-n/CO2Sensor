#Initialization
kport = ["GPIB::1","GPIB::2"] #sourcemeter external port
svr = 1 #source voltage range
comc=.1 #compliance current
data = open('log1', mode='w') #output file
points=50 #data points collected
ts=.001 #timestep