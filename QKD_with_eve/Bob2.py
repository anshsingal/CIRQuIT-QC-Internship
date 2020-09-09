import random
bob_bases = ""
random.seed(84)
def bob_measure_qubit(num_qubits, qubit_circuit):
    bob_bases = str('{:050b}'.format(random.getrandbits(num_qubits)))
#     print(bob_bases)
    bob_qubit_circuits = []
#     print(bob_bases)
    for i, qubit in zip(bob_bases.strip(), qubit_circuit):
        circ = update_circuits(qubit, int(i))
        bob_qubit_circuits.append(circ)
    return bob_qubit_circuits, bob_bases
    
def update_circuits(qubit, hadamard_basis):
    if hadamard_basis:
        qubit.h(0)
    qubit.measure(0,0)
    return qubit