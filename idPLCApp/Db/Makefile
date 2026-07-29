TOP=../..
include $(TOP)/configure/CONFIG

DB += NX102_tilt.template
DB += NX102_tiltpot.template
DB += NX102_id.template
DB += NX102_idoverrides.template
DB += NX102_idpotscan.template
DB += idplc_status.template
DB += idplc_axisEna.template
DB += idplc_gui.template

DB += NX102_axisexp.template

ifeq ($(EPICS_BASE),/dls_sw/epics/R3.14.12.7/base)

FLATDB=flatdb

else

FLATDB="EPICS_DB_INCLUDE_PATH=.:.. flatdb.sh "

NX102_axisexp.template: NX102_axisexp.vdb
	$(FLATDB) --disable-macro-warnings $< $@

endif

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
