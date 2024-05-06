# Neural Network Implementation in Python

This repository contains a simple implementation of a neural network in Python using NumPy. The neural network is designed to model a single neuron with three input connections and one output connection.

## Getting Started

### Prerequisites

To run the code, you need to have Python 3 installed on your system. Additionally, you'll need to install NumPy, a powerful numerical computing library in Python.

You can install NumPy using pip:

```bash
pip install numpy
```

### Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/neural-network-python.git
```

2. Navigate to the project directory:

```bash
cd neural-network-python
```

3.Run the neural network:

```bash
python neural_network.py
```

This will train the neural network using a predefined training set and then test it with a new situation.

## Neural Network Architecture

The neural network implemented here consists of:

- **Single Neuron**: Modeled with three input connections and one output connection.
- **Sigmoid Activation Function**: Used to introduce non-linearity and normalize outputs between 0 and 1. ![Image Alt Text](media\1_HDWhvFz5t0KAjIAIzjKR1w.webp)
- **Backpropagation**: Training the network involves adjusting synaptic weights based on the error between predicted and actual outputs.

## Files Included

- `neural_network.py`: Python script containing the neural network implementation.
- `README.md`: This README file providing information about the project.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
