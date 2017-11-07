#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def estimate_e(N=100000):
    """Takes parameter N which is the number of points on the x axis for the integral of e^x
    Returns a float that is an estimate of e"""
    xs = np.random.uniform(0,1,N)
    return np.exp(xs).sum()/N +1