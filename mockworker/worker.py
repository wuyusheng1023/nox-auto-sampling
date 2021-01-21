from copy import copy

import numpy as np

from .data import NOX_ANALYZER, MFC_SETPOINT, UPS


mfc = {'set': MFC_SETPOINT, 'read': 0}
ups = UPS


def get_random_coef():
  pass


class NOxAnalyzer():

  def __init__(self, data=None):
    self.data = copy(NOX_ANALYZER)

  def _get_raw_data(self):
    self.data = None
