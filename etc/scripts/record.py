#!/dls_sw/prod/python3/RHEL7-x86_64/softioc/4.4.0/prefix/bin/pythonSoftIOC
#
# script to record pot positions
#
# set up pots
import sys
import cothread
import epicscorelibs.path.cothread
from cothread.catools import caget, camonitor, caput
from cothread.cothread import Sleep

output=open("data-scan-2026-05-28-500um.txt","w")
demand = "TS02K-MO-SERVC-01:CS:GAP"
start_gap = 4
step=.5
end_gap = 100
gap = start_gap
index = 0

# for axis in range(1,5):
#     potClear(axis)

okay=True
while okay:
    print(f"caput for gap {gap}")
    caput(demand, gap, wait=True, timeout=10)
    print("caput done")
    Sleep(2)
    for axis in range(1,5):
        encoderPv = f"TS02K-MO-SERVO-0{axis}:MOT.RBV"
        rawPv = f"TS02K-MO-AXIS-0{axis}:RAW"
        pot=caget(rawPv)
        enc=caget(encoderPv)
        print(gap, axis, pot, enc, file=output)
        print(gap, axis, pot, enc, file=sys.stdout)
        #program(index,axis, pot, enc)
    print(f"programming index {index} done", file=sys.stdout)
    gap = gap + step
    index += 1
    if step > 0:
        if gap > end_gap:
            okay = False
    else:
        if gap < end_gap:
            okay = False

# for axis in range(1,5):
#     moveToMain(axis)


output.close()
