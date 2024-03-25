# data_preprocessing implementation details

The ```data_preprocessing``` package includes a Python module, ```utils.py```, that implements data integration related functions the TEG detectors.

## utils module
The ```utils``` module includes the following functions:
| function            					  |    description														|
|----------------------------------------------------------------------------------------------- |----------------------------------------------------------------------------------   |
| get_configuration() | Returns the data source configuration defined in data_source_config.yaml file within the config sub-directory of the same package. The returned configuration contains a brief description of dataset and the path to the file containing the data set. |
| read_data_from_csv() | Reads the data from the .csv file which has its path specified in the data_source_path field of the data configuration, defined in ```data/config/data_source_config.yaml.``` The dataset is returned as a ```pandas Dataframe``` with 2 columns: ```timestamp``` and ```value```, as we use equi-width histograms to model the date distribution over a given time period. |
| preprocess_value(val, max_val) | Maps the value given as parameter through val to an integer between 0 and 100 as follows: the value is divided by the maximum value, also given as parameter, and the result is multiplied by 100 and then rounded. This step of preprocessing is needed because of the constraints of Concrete Fully Homomorphic Encryption library in terms of size and type of the inputs. |
| rescale_data(df) 	|Preprocesses each data sample within a dataset given as parameter using the ```preprocess_value(val, max_val)``` function. |
| get_anomalies_index(data, labels) | It is an auxiliary function which, given the data to be labeled and the labels generated after detecting anomalies within that specific dataset, returns the indices of anomalies in the input dataset and their values. It is used at plotting abnormal values on the same graph as the input dataset. |
| plot_data_and_anomalies(data, ref_data, labels) | This function plots the reference data and the data to be labeled on the same graph, also pointing the anomalies out. |
| plot_histograms(data, ref_data, n_bins, min, max) | Given the data to be labeled, the reference data the number of buckets in the histogram and the minimum and maximum allowed values, this functions plotts the equi-width histogram of both reference data and data to be labeled on the same graph. |