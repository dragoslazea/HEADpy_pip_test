import numpy as np
import pandas as pd
import math as math
from concrete import fhe
from .utils import get_configuration
import histo_building.builder as builder
import histo_building.utils as build_utils

def is_in_abnormal_bucket(x, freq, low, high, th): # checks if x is in an abnormal bucket, based on a threshold
  is_greater = x > low
  is_eq_low = x == low
  is_less = x < high
  is_abnormal = freq < th

  result = (is_greater + is_eq_low) * is_less * is_abnormal * 1

  return result

vabnormal = np.vectorize(is_in_abnormal_bucket)

def clear_abnormal_labels(x, f, l, h, th):
  al = []
  for xi in x:
    is_greater100 = xi > 100
    al.append(vabnormal(xi, f, l, h, th).sum() + (is_greater100 * 1))
  return al

def crypto_abnormal_labels(x, f, l, h, th):
  al = []
  for xi in x:
    al.append(vabnormal(xi, f, l, h, th).sum())
  return fhe.array(al)

def build_histo_abnormal_labels(x, y, l, h, th):
  hi = builder.build_clear_histogram(y, l, h).tolist()
  al = []
  for xi in x:
    al.append(vabnormal(xi, hi, l, h, th).sum())
  return al

def crypto_build_histo_abnormal_labels(x, y, l, h, th):
  hi = builder.build_clear_histogram(y, l, h).tolist()
  al = []
  for xi in x:
    al.append(vabnormal(xi, hi, l, h, th).sum())
  return fhe.array(al)

def create_inputset_detector(train_samples, ref_histo):
  config = get_configuration()

  (l, h) = build_utils.build_buckets(config['reference_histogram']['bin_size'], config['reference_histogram']['min'], config['reference_histogram']['max'])

  inputset = []

  for d in train_samples:
    inputset.append((d, ref_histo, l, h, config['threshold']))
  
  return inputset

def create_inputset_builder_and_detector(detect_samples, build_samples):
  config = get_configuration()

  (l, h) = build_utils.build_buckets(config['reference_histogram']['bin_size'], config['reference_histogram']['min'], config['reference_histogram']['max'])

  inputset = []

  for i in range(len(detect_samples)):
    inputset.append((detect_samples[i], build_samples[i], l, h, config['threshold']))
  
  return inputset