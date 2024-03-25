import pandas as pd
import yaml
import os
import matplotlib.pyplot as plt
import numpy as np

# parse the yaml file to get the configuration for the data source the histogram
def get_configuration():
  absolute_path = os.path.dirname(__file__)
  relative_path = "config/data_source_config.yaml"
  full_path = os.path.join(absolute_path, relative_path)
  with open(full_path, "r") as config_file:
      config = yaml.safe_load(config_file)
  return config

# read a csv file and return the data as a pandas dataframe
def read_data_from_csv():
    config = get_configuration()
    df = pd.read_csv(config['data']['data_source_path'])
    df.columns = ["timestamp", "value"]
    return df

# transform a value to an integer in [0, 100]
def preprocess_value(val, max_val):
    return round((val / max_val) * 100)

# rescale all the values in the "value" column to values between 0 and 100
def rescale_data(df):
    dlist = df["value"].tolist()
    max_val = max(dlist)
    preprocessed_data = [preprocess_value(i, max_val) for i in dlist]
    df["value"] = preprocessed_data

# get the list of data samples recorded during a day (in our example dataset the format of the timestamp fiels is "mm/dd/yyyy hh:mm")
def get_data_by_day(df, day):
    dfd = df[(df["timestamp"].astype(str)).str.startswith(day)]
    return dfd['value'].tolist()

def get_anomalies_index(data, labels):
  an = []
  xn = []

  for i in range(len(data)):
    if labels[i] == 1:
      an.append(data[i])
      xn.append(i)

  return (xn, an)

def plot_data_and_anomalies(data, ref_data, labels):
  (xn, an) = get_anomalies_index(data, labels)
  x = np.arange(0, len(data))
  plt.figure(figsize=(10,4))
  plt.scatter(x, ref_data, color="green", label="reference data")
  plt.scatter(x, data, color="blue", label="data to be labeled")
  plt.scatter(xn, an, marker="*", color="red", label="anomalies")
  plt.legend()

  plt.xlabel("Time (every hour)")
  plt.ylabel("Smart meter reading")

  plt.show()

def plot_histograms(data, ref_data, n_bins, min, max):
  plt.figure(figsize=(10,4))
  plt.hist(data, bins=n_bins, color='red', range=(min, max), alpha=0.5, edgecolor='black', label='processed data histogram')
  plt.hist(ref_data, bins=n_bins, color='skyblue', range=(min, max), alpha=0.5, edgecolor='black', label='reference histogram')

  plt.xlabel('Smart meter measurement range')
  plt.ylabel('Frequency')
  plt.legend()

  plt.show()