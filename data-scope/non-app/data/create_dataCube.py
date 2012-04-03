#!/usr/local/bin/python2.7
# encoding: utf-8

# choose a start time
t0 = DT.datetime(2010, 1, 1)

# convert to time tuple
t0 = t0.utctimetuple()

# convert t0 to UNIX time in milliseconds 
t0 =  int(1000 * time.mktime(t0))

# choose a time step
timeStep = 60*60*1000        # milliseconds in one hour

# choose end time 
tfin = int(1000 * time.time())

# create the first column in the fact table
timeCol = NP.arange(t0, tfin, timeStep)
timeCol.shape
(18620,)
x = timeCol[100]
x
1262660400000
x = timeCol[250]
x
1263200400000
x = time.gmtime(x)
x
time.struct_time(tm_year=41999, tm_mon=3, tm_mday=25, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=84, tm_isdst=0)
x = timeCol[250]
x /= 1000
x = time.gmtime(x)
x
time.struct_time(tm_year=2010, tm_mon=1, tm_mday=11, tm_hour=9, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=11, tm_isdst=0)
len(x)
9
a, b, c, d, e, f, g, h, i = time.gmtime(timeCol[250]/1000)
a
2010
b
1
c
11
d
9
e
0
f
0
