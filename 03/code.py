import pathlib
from typing import List

FILE_PATH = pathlib.Path(__file__).parent / "input_files" / "input.txt"

def unsigned_elementwise_not(x: int, size: int) -> int:
    mask = int('1' * size, 2)
    return mask ^ x

def read_input():
    with open(FILE_PATH, 'r') as f:
        raw_binary_inputs = f.read().splitlines()
        binary_input_bits = [[int(x) for x in list(x_raw)] for x_raw in raw_binary_inputs]
        
        return binary_input_bits
    
def get_most_common_bits(input_sequences: List) -> int:
    num_of_sequences = len(input_sequences)
    sequence_length = len(input_sequences[0])
    
    num_ones = [int(sum([x[i] for x in input_sequences]) > (num_of_sequences / 2)) for i in range(sequence_length)]
    return int(''.join([str(x) for x in num_ones]), 2)

def calculate_rates():
    input_data = read_input()
    
    gamma_rate = get_most_common_bits(input_data)
    epsilon_rate = unsigned_elementwise_not(gamma_rate, len(input_data[0]))
    
    print(f"Gamma rate: {gamma_rate}")
    print(f"Epsilon rate: {epsilon_rate}")
    print(f"Power Consumption: {gamma_rate * epsilon_rate}")
    
if __name__ == '__main__':
    calculate_rates()