# Author: Khoi Tran
# Date: 2025-05-10
# Description: We use Qiskit to implement a quantum version of the Blackjack game.
# The game is played between a player and a dealer. The player can choose to hit or stand.
# The dealer will reveal their hand and the player will win if their hand is closer to 21 than the dealer's hand.

# The game uses quantum circuits to simulate the randomness of card drawing.
# The player and dealer's hands are represented as quantum states, and the game logic is implemented using Qiskit.
# The game is played in a Jupyter notebook environment, and the player can interact with the game using a simple command line interface.
# THIS IS A PYTHON FILE VERSION OF THE GAME

## BEFORE RUNNING THE CODE, MAKE SURE YOU HAVE THE FOLLOWING LIBRARIES INSTALLED: QISKIT AND QISKIT-AER
# You can install them using pip:
# pip install qiskit
# pip install qiskit-aer

from qiskit import QuantumCircuit
from qiskit_aer import Aer

def draw_card():
    # Create a quantum circuit with 4 qubits
    qc = QuantumCircuit(4)
    qc.h(range(4))  # Apply Hadamard gate to put qubits in superposition
    qc.measure_all()  # Measure all qubits

    # Use the Aer simulator to execute the circuit
    simulator = Aer.get_backend('qasm_simulator')
    job = simulator.run(qc, shots=1)  # Run the circuit with 1 shot
    
    # Get the result of the measurement
    result = job.result() 
    counts = result.get_counts()

    # Convert the measured binary string to an integer (1-10 for card values)
    binaryResult = list(counts.keys())[0]
    cardValue = int(binaryResult, 2) % 10 + 1
    return cardValue


def play_blackjack():
    print("Quantum Blackjack Starts!")
    
    player = [draw_card(), draw_card()]
    dealer = [draw_card(), draw_card()]

    print(f"You drew: {player} (total: {sum(player)})")
    print(f"Dealer shows: [{dealer[0]}, ?]")

    while sum(player) < 21:
        move = input("Hit or stand? (enter h or s): ").lower()
        if move == 'h':
            card = draw_card()
            player.append(card)
            print(f"You drew {card}, total is now {sum(player)}")
            if sum(player) > 21:
                print("Bust! You lose.")
                return
        elif move == 's':
            print("You chose to stand.")
            break
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand.")

    print(f"Dealer's cards: {dealer} (total: {sum(dealer)})")
    
    # Dealer's turn: must hit until total is 17 or more
    while sum(dealer) < 17: 
        card = draw_card()
        dealer.append(card)
        print(f"Dealer draws {card}, total: {sum(dealer)}")
    
    playerTotal = sum(player)
    dealerTotal = sum(dealer)
    print(f"\nFinal Score — You: {playerTotal} | Dealer: {dealerTotal}")
    if dealerTotal > 21 or playerTotal > dealerTotal:
        print("Congratulation.. You win!")
    elif dealerTotal == playerTotal:
        print("It's a tie.")
    else:
        print("You lose.. Better luck next time!")

# Start the game
if __name__ == "__main__":
    play_blackjack()