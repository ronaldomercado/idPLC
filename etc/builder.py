from iocbuilder import AutoSubstitution, ModuleBase, records, Device, Xml

# templates related to ID interface
class NX102_tilt(AutoSubstitution):
    TemplateFile = 'NX102_tilt.template'

class NX102_tiltpot(AutoSubstitution):
    TemplateFile = 'NX102_tiltpot.template'

class NX102_axisexp(AutoSubstitution):
    TemplateFile = 'NX102_axisexp.template'

class NX102_id(AutoSubstitution):
    TemplateFile = 'NX102_id.template'

class NX102_idoverrides(AutoSubstitution):
    TemplateFile = 'NX102_idoverrides.template'

class NX102_idpotscan(AutoSubstitution):
    TemplateFile = 'NX102_idpotscan.template'
    
class Status(AutoSubstitution):
    TemplateFile = 'idplc_status.template'

class AxisEnable(AutoSubstitution):
    TemplateFile = 'idplc_axisEna.template'
