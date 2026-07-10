TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# In a Diamond Support Module, install
# templates like this
#
#DB += motor.template
#DB += basic_motor.template

#----------------------------------------------------
# In a Diamond IOC Application, build db files from
# template files like this
#
DB += NX102_tilt.template
DB += NX102_tiltpot.template
DB += NX102_axisexp.template
DB += NX102_id.template
DB += NX102_idoverrides.template
DB += NX102_idpotscan.template
DB += idplc_status.template
DB += idplc_axisEna.template

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
