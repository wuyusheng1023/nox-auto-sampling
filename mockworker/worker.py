from copy import copy

import numpy as np

from .data import NOX_ANALYZER, MFC_SETPOINT, UPS


mfc = {'set': MFC_SETPOINT, 'read': 0}
ups = UPS


def get_random_coef():
  x = np.random.normal(1, 0.0025)
  x = 1.0075 if x > 1.0075 else x
  x = 0.9925 if x < 0.9925 else x
  return x


class NOxAnalyzer():

  def __init__(self, data=None):
    self.data = copy(NOX_ANALYZER)

  def _get_raw_data(self):
    # self.data = None
    pass
