import argparse
from mutators import RandomMutator, QFTMutator, UCNOTMutator
from line import Circuit

parser = argparse.ArgumentParser(description="Quantum Test Case Generator QuraTest")

parser.add_argument("-n", type=int, default=5, help="number of qubits")
parser.add_argument("-m", choices=['random', 'qft', 'ucnot'], help='quantum test case generator')
parser.add_argument("-o", type=str, default='output.s', help='output path of generated test case')

args = parser.parse_args()

if args.m == 'random':
    mutator = RandomMutator()
elif args.m == 'qft':
    mutator = QFTMutator()
elif args.m == 'ucnot':
    mutator = UCNOTMutator()

circuit = Circuit(args.n)
new_circuit = mutator.generate_circuit(circuit)
# if you want to output 
print(new_circuit.code)
result = new_circuit.run_vec()
print(result[0].real)
print(result[0].imag)