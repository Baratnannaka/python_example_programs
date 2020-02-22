#program to find simple intrest
#enter prince in rupes
P=input('enter price in rupes: ')

#enter rate in rupes
R=input('enter intrest rate in rupes: ')

#enter time durestion
T=input('enter time in manths: ')

#cleculation
SI = (P * R * T) / 100

#for one manth
STFM = SI/12

#for one day
STFD = STFM/30

#print the resultentvalue of SI
print "simple intrest is", SI

print "simple intrest for Month is", STFM

print "simple intrest for day is ", STFD
