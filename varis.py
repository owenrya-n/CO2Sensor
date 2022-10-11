#Initialization
kport = ["GPIB::1","GPIB::2"] #sourcemeter external port
svr = 1 #source voltage range
comc=.1 #compliance current
data = open('test.txt', mode='w') #output file
rvtg=1