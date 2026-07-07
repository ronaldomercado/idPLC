#!/dls_sw/prod/python3/RHEL7-x86_64/softioc/4.4.0/prefix/bin/pythonSoftIOC

# set up pots
import cothread
import epicscorelibs.path.cothread
from cothread.catools import caget, camonitor, caput
from cothread.cothread import Sleep
import sys

# main
if len(sys.argv) < 2:
    print(f"usage: {sys.argv[0]} <axis>\n\nwhere axis is a value from 1 to 4")
    sys.exit(1)

axis = int(sys.argv[1])
print(f"Axis {axis}")
indexPv=f"TS02K-MO-AXIS-0{axis}:PS:INDEX"
potvaluePV=f"TS02K-MO-AXIS-0{axis}:PS:POT"
encvaluePV=f"TS02K-MO-AXIS-0{axis}:PS:ENC"
i=0
while True:
    caput(indexPv,i)
    Sleep(2)
    pot=caget(potvaluePV)
    enc=caget(encvaluePV)
    print(f" {i} pot={pot} enc={enc}")
    if pot == -1:
        break
    else:
        i = i+1
        Sleep(0.5)
    
