from copy import copy

from data import NOX_ANALYZER, MFC_SETPOINT, UPS


nox = copy(NOX_ANALYZER)
mfc = {'set': MFC_SETPOINT, 'read': 0}
ups = UPS

print(f"""
NOx Analyzer: {nox}
MFC: {mfc}
UPS: {UPS}
""")
