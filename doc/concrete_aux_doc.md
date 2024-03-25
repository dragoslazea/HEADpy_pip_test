# concrete_aux implementation details

The ```concrete_aux``` package includes a Python module, ```fhe_utils.py```, that implements the functions used at interacting with Concrete circuits.

## fhe_utils module
The ```fhe_utils``` module includes the following functions:
| function            					  |    description														|
|----------------------------------------------------------------------------------------------- |----------------------------------------------------------------------------------   |
| compile_circuit(function_name, params, inputset) | This function, given the name of a function, the set of its parameters and a set of training data, generates and compiles a Concrete circuit implementing a lookup table which simulates the behaviour of the function. The parameters of the function should be provided as a dictionary with elements having the following structure: ```“formal_parameter”: “encrypted”```. The function returns the circuit compiled using the training data provided as parameter. |
| apply_circuit(circuit, data_sample) | This function applies the Concrete circuit given as parameter on the given input data sample. It encrypts the input data, applies the circuit and computes the encrypted result.  |
| check_results(circuit, clear_func, data_sample) | It returns true if the result of applying the circuit on the given data is equal, after decrypting, to the result of applying the corresponding clear function, clear_func, on the same data.  |
