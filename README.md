# Quantum Blackjack - Qiskit
This is a simple Blackjack game powered by quantum randomness using IBM's Qiskit framework.

## How Does Quantum Computing Work?
**Classical computers** performs calculations and operations using **bits**: 0 or 1. 
**Quantum computers**, on the other hand, handle them using **qubits**, which can be in **superposition**: both 0 and 1 at the same time.
- Due to its nature, quantum computers are **a lot faster** than traditional computers, but they also require **more energy** to execute an operation.
- Qubits can also be **entangled**, meaning one affects the other.
- When measured, a qubit 'collapses' to either 0 or 1.

The difference between a classical bit is similar to a coin on the table where the result is either head or tail, while a qubit is like a spinning coin, having the value being both head and tail simultaneously.

## Before you start
- Please make sure that you have **Python 3.10+** installed. Tested version: **Python 3.10.16**
- Additionally, I requirement installing **Conda/Miniconda** for Python environment for this project. This is to make sure the newly install required packages won't mess up the base Python environment. Documents can be found here:

    https://www.anaconda.com/docs/getting-started/miniconda/install#windows-installation
  
## Install required Python packages (must-do)
pip install qiskit
pip install qiskit-aer

# Reference Pages: 
- QuantumCircuit: https://docs.quantum.ibm.com/api/qiskit/circuit
- measure_all: https://docs.quantum.ibm.com/guides/measure-qubits
- Aer simulator: https://qiskit.github.io/qiskit-aer/tutorials/1_aersimulator.html
- Python List: https://www.w3schools.com/python/python_lists.asp
