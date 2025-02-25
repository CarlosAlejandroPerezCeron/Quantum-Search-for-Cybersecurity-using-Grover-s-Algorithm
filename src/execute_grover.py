from qiskit import Aer, execute
from grover_main import create_grover_circuit
from oracle import apply_oracle
from diffuser import apply_diffuser
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def run_grover():
    qc = create_grover_circuit()
    apply_oracle(qc)
    apply_diffuser(qc)
    qc.measure_all()

    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1024).result()
    counts = result.get_counts()
    plot_histogram(counts)
    plt.show()

if __name__ == "__main__":
    run_grover()
