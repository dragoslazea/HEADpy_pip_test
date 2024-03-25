import yaml
import os

# function to build the lists of low and high values of the buckets, given the size and the min and max values
def build_buckets(size, min_val, max_val):
  low = min_val
  l = [min_val]
  while (low + size < max_val):
    low = low + size
    l.append(low)

  h = []
  for ll in l:
    h.append(min(ll + size, max_val))

  return (l, h)

# parse the yaml file to get the configuration for building the histogram
def get_configuration():
  absolute_path = os.path.dirname(__file__)
  relative_path = "config/histogram_build_config.yaml"
  full_path = os.path.join(absolute_path, relative_path)
  with open(full_path, "r") as config_file:
      config = yaml.safe_load(config_file)
  return config