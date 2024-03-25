# histo_building implementation details

The ```histo_building``` package includes two Python modules
- ```builder.py```: implements the histogram building related functions;
- ```utils.py```: provides auxiliary functions, used at creating the histogram.

## builder module
Within the ```builder``` module, the following functions are implemented:
| function            					  |    description														|
|----------------------------------------------------------------------------------------------- |----------------------------------------------------------------------------------   |
| is_in_bucket(x, low, high) | Checks if ```x``` is in the range defined by ```low``` and ```high``` parameters (i. e. ```x``` is in ```[low```, ```high)```). It returns 1 if the value fits in the given range and 0 otherwise. |
| vbucket(x, low, high) | Returns a one-hot vector, containing a single value of 1, placed on the position corresponding to the range x fits in and 0 on all the other positions. Given an input value ```x``` and two lists of ```low``` and ```high``` values, this function applies is_in_bucket function on each triplet ```(x, low[i], high[i])``` in a vectorial fashion. |
| build_clear_histogram(x, l, h) | Builds the equi-width histogram of the dataset represented by the list ```x``` using the ranges given by ```l``` and ```h```. Each pair of values ```(l[i], h[i])``` represents the range of a specific bucket. The function returns the equi-width histogram as a list of the same size as ```l``` and ```h```, containing on ```ith``` position the number of elements in ```x``` that fit into the ```[l[i], h[i])``` range. |
| build_crypto_histogram(x, l, h) | The cryptographic version of  build_clear_histogram. Returns the histogram as a ```fhe.array.``` |
| create_inputset(train_samples) | Given a list of training sets, this function creates an input set which can be used to train a Concrete histogram building circuit. For each training set, ```values```, we compute a triplet ```(values, low, high)```, where ```low``` and ```high``` are lists containing the ranges of buckets defined according to the configuration defined in ```histogram_build_config.yaml```. The function returns the list of triplets corresponding to all training sets in the input list. |


## utils module
The ```utils``` module includes the following functions:
| function            					  |    description														|
|----------------------------------------------------------------------------------------------- |----------------------------------------------------------------------------------   |
| get_configuration() | It is a function which returns the configuration defined in ```histogram_build_config.yaml``` file within the config sub-directory of the same package. It defines the size of a bucket and the global minimum and maximum values. |
| build_buckets(size, min_val, max_val) | Given the size of a bucket and the minimum and maximum values which can be encountered within the data, this function returns a pair of lists containing the sub-ranges of ```[min_val, max_val)``` corresponding to the ranges of the buckets of size given as an input parameter. |