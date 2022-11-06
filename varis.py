#Initialization
kport = ["GPIB::1"] #sourcemeter external port
#kport = ["GPIB::1","GPIB::2"] #sourcemeter external port
svr = 2 #source voltage range
comc=.1 #compliance current
file = 'data.csv'
points=5 #data points collected
ts=.01 #timestep
resistance = 470000 #derived experimentally for cap exp
Ht=2 #function generation
Lt=.2 #function generation