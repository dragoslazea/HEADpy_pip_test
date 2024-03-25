from concrete import fhe

def compile_circuit(function_name, params, inputset):
  compiler = fhe.Compiler(function_name, params)

  configuration = fhe.Configuration(
      comparison_strategy_preference=fhe.ComparisonStrategy.ONE_TLU_PROMOTED,
  )

  print(f"Compiling...")
  circuit = compiler.compile(inputset, configuration, show_mlir=False, show_statistics=False)

  print(f"Generating keys...")
  circuit.keygen()

  return circuit

def apply_circuit(circuit, data_sample):
  encrypted_example = circuit.encrypt(*data_sample)
  encrypted_result = circuit.run(encrypted_example)

  return encrypted_result

def check_results(circuit, clear_func, data_sample):
  encrypted_result = apply_circuit(circuit, data_sample)

  decrypted_result = circuit.decrypt(encrypted_result)
  clear_result = clear_func(*data_sample)

  return all(x == y for x, y in zip(decrypted_result, clear_result))