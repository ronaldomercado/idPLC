#!/dls_sw/prod/python3/RHEL7-x86_64/softioc/4.4.0/prefix/bin/pythonSoftIOC
#
# script to capture and print a row of values from the sensors
#
import sys
import cothread
import epicscorelibs.path.cothread
from cothread.catools import caget, camonitor, caput
from cothread.cothread import Sleep

for axis in range(1,5):
    gapPv = "TS02K-MO-SERVC-01:CS:GAP.RBV"
    encoderPv = f"TS02K-MO-SERVO-0{axis}:MOT.RBV"
    rawPv = f"TS02K-MO-AXIS-0{axis}:RAW"
    gap=caget(gapPv)
    pot=caget(rawPv)
    enc=caget(encoderPv)
    print(gap, axis, pot, enc, file=sys.stdout)
