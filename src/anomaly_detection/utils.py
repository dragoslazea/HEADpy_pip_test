import yaml
import os

# parse the yaml file to get the configuration for building the histogram
def get_configuration():
  absolute_path = os.path.dirname(__file__)
  relative_path = "config/anomaly_detection_config.yaml"
  full_path = os.path.join(absolute_path, relative_path)
  with open(full_path, "r") as config_file:
      config = yaml.safe_load(config_file)
  return config