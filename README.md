# QuraTest

QuraTest is an input generator for quantum programs.

## Requirements

* Python==3.8.19
* qiskit==0.31.0

## Running Instruction

```python main.py -n 5 -m qft -o output.qasm```

Arguments:
* n: the number of the qubits you want
* m: mutators to use. Three mutators are provided: random, qft, ucnot
* o: output file
