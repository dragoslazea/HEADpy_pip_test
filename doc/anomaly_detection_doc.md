# anomaly_detection implementation details

The ```anomaly_detection``` package includes two Python modules
- ```detector.py```: implements several functions used at detecting anomalies based on equi-width histogram of both clear and encrypted data;
- ```utils.py```: provides auxiliary functions, used during the anomaly detection process.

## detector module
Within the ```builder``` module, the following functions are implemented:
| function            					  |    description														|
|----------------------------------------------------------------------------------------------- |----------------------------------------------------------------------------------   |
| is_in_abnormal_bucket(x, freq, low, high, th) | Checks if the ```x``` is in the range defined by ```low``` and ```high``` parameters (i. e. ```x``` is in ```[low```, ```high)```) and if the value of the ```freq``` parameter is lower than a threshold, ```th```. If both conditions are satisfied, it returns 1 and 0 otherwise. |
| vabnormal(x, freq, low, high) | Given two input values ```x``` and ```th``` and three lists, ```low```, ```high``` and ```freq```, this function applies ```is_in_abnormal_bucket``` function on each tuple ```(x, freq[i], low[i], high[i], th)``` in a vectorial fashion. It returns a one-hot vector, containing a single value of 1, placed on the position corresponding to the range x fits in if the value in freq on the same position is lower than ```th``` and a list of 0s otherwise. |
| clear_abnormal_labels(x, f, l, h, th) | Labels each sample in the dataset represented by the list ```x``` using the ranges given by ```l``` and ```h```. Each triplet of values ```(f[i], l[i], h[i])``` represents a specific bucket defined by the number of elements within the bucket and the range of the bucket. The function returns a list of the same size as ```l``` and ```h```, containing on ith position the label associated to ```x[i]``` (0 – normal value, 1 – abnormal value). |
| crypto_abnormal_labels(x, f, l, h, th) | This function is the cryptographic version of ```clear_abnormal_labels``` which returns list of labels as a ```fhe.array.``` |
| build_histo_abnormal_labels(x, y, l, h, th) | Builds the histogram of a reference dataset, ```y```, using the ranges given by ```l``` and ```h```, based on which it detects anomalies in another dataset ```x``` using a frequency threshold, ```th```. It outputs the list of labels corresponding to data samples in ```x```. |
| crypto_build_histo_abnormal_labels(x, y, l, h, th) | It is the cryptographic version of ```build_histo_abnormal_labels```. |
| create_inputset_detector(train_samples, ref_histo) | Given a list of training sets and a reference histogram, this function creates an input set which can be used to train a Concrete histogram-based anomaly circuit. For each training set, ```values```, computes a tuple ```(values, ref_histo, low, high, config.threshold)```, where ```low``` and ```high``` are lists containing the ranges of buckets in the reference histogram, defined according to the configuration defined in ```anomaly_detection_config.yaml```, and ```config.threshold``` is the threshold value define in the same configuration. The function returns the list of tuples corresponding to all training sets in the input list. |
| create_inputset_builder_and_detector(detect_samples, build_samples) | Given a list of training sets for detecting anomalies and a list of training samples for building the histogram, this function creates an input set which can be used to train a Concrete circuit which builds a histogram using the build_samples and detects anomalies in ```detect_samples``` based on that histogram. For each pair of training sets, ```(detect_values, build_values)```, placed on the same position in the input lists of training sets, we compute a tuple ```(detect_values, build_values, low, high, config.threshold)```, in a totally similar way to create_inputset_detector function. |

## utils module
The ```utils``` module includes the following functions:
| function            					  |    description														|
|----------------------------------------------------------------------------------------------- |----------------------------------------------------------------------------------   |
| get_configuration() | Returns the configuration defined in ```anomaly_detection_config.yaml``` file within the config sub-directory of the same package. The returned configuration defines the size of a bucket and the global minimum and maximum values in the reference histogram and the threshold value based on which the data is labeled. |
