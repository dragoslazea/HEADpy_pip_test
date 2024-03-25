import numpy as np
import pandas as pd
import math as math
from concrete import fhe
from .utils import build_buckets, get_configuration

# checks if x is in [low, high)
def is_in_bucket(x, low, high): 
  is_greater = x > low
  is_eq_low = x == low
  is_less = x < high

  result = (is_greater + is_eq_low) * is_less * 1

  return result

# vectorial is_in_bucket 
vbucket = np.vectorize(is_in_bucket)

# clear histogram_building
def build_clear_histogram(x, l, h):
  hi = 0
  for xi in x:
    hi = hi + vbucket(xi, l, h)
  return hi

# cryptographic histogram building
def build_crypto_histogram(x, l, h):
  hi = 0
  for xi in x:
    hi = hi + vbucket(xi, l, h)
  return fhe.array(hi)

def create_inputset(train_samples):
  config = get_configuration()

  (l, h) = build_buckets(config['histogram']['bin_size'], config['histogram']['min'], config['histogram']['max'])
  inputset = []

  for d in train_samples:
    inputset.append((d, l, h))

  return inputset