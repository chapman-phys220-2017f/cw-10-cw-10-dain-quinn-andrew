#!/usr/bin/env python3

import numpy as np
import estimate_e as ee
def test_estimate_e():
    """Tests the estimate_e(N=100000) function."""
    actual = np.e
    trial = ee.estimate_e(10000000)
    print("Testing if actual = "+str(actual)+" ?= trial = "+str(trial))
    np.testing.assert_allclose(actual, trial,0.001)
    