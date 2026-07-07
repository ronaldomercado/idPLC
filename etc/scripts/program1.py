#!/dls_sw/prod/python3/RHEL7-x86_64/softioc/4.4.0/prefix/bin/pythonSoftIOC
# program to program the potentiometers for axis 1
# using extrapolated data
import cothread
import epicscorelibs.path.cothread
from cothread.catools import caget, camonitor, caput
from cothread.cothread import Sleep
import sys

def potClear(axis):
    caput(f"TS02K-MO-AXIS-0{axis}:PS:CLEAR.PROC",1)

def program(index, axis, pot, enc):
    indexPv=f"TS02K-MO-AXIS-0{axis}:PS:INDEX"
    caput(indexPv,index)
    potvaluePV=f"TS02K-MO-AXIS-0{axis}:PS:OUT:POT"
    encvalueOutPV=f"TS02K-MO-AXIS-0{axis}:PS:OUT:ENC"
    caput(potvaluePV, pot)
    caput(encvalueOutPV, enc)
    Sleep(1)
    caput(f"TS02K-MO-AXIS-0{axis}:PS:SETIDX.PROC", 1)
    Sleep(1)
    
def parse(line):
    elems=line.split()
    gap=float(elems[0])
    axis=int(elems[1])
    pot=float(elems[2])
    enc=float(elems[3])
    return (gap, axis, enc, pot)

def moveToMain(axis):
    caput(f"TS02K-MO-AXIS-0{axis}:PS:END.PROC",1)

datafile = "data-scan-extrapolated.txt"
#datafile="ds.txt"
df = open(datafile, "r")
ax1 = df.readline()
ax2 = df.readline()
ax3 = df.readline()
ax4 = df.readline()
dataReady = ax1 != '' and \
    ax2 != '' and \
    ax3 != '' and\
    ax4 != ''
index = 0


potClear(1)

while dataReady:
    print(f"Programming index {index}", file=sys.stdout)
    gap, axis, enc, pot = parse(ax1)
    program(index,axis, pot, enc)
    print(f"gap {gap} axis {axis} pot {pot} enc {enc}", file=sys.stdout)

    print(f"programming index {index} done", file=sys.stdout)
    ax1 = df.readline()
    ax2 = df.readline()
    ax3 = df.readline()
    ax4 = df.readline()

    dataReady = ax1 != '' and \
        ax2 != '' and \
        ax3 != '' and\
        ax4 != ''
    if dataReady:
        index += 1

moveToMain(1)
