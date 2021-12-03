from enum import Enum
import pathlib
from typing import List

FILE_PATH = pathlib.Path(__file__).parent / "input_files" / "input.txt"

class Criterion(Enum):
    MOST_COMMON = 1
    LEAST_COMMON = 2
    
class Rate(Enum):
    OXYGEN_GENERATOR = Criterion.MOST_COMMON
    CO2_SCRUBBER = Criterion.LEAST_COMMON
    
def read_input():
    with open(FILE_PATH, 'r') as f:
        raw_binary_inputs = f.read().splitlines()
        binary_input_bits = [[int(x) for x in list(x_raw)] for x_raw in raw_binary_inputs]
        
        return binary_input_bits
    
def get_most_common_bit(bits: List[int]):
    num_of_zeros = bits.count(0)
    num_of_ones = bits.count(1)
    
    if num_of_zeros > num_of_ones:
        return 0
    elif num_of_zeros <= num_of_ones:
        return 1
    
def bitlist_to_int(bits: List[int]):
    return int(''.join(map(str, bits)), 2)
    
def filter_by_criterion(input_data: List[List[int]], bit_index: int, criterion: Criterion):
    # find the most common bit
    bits_at_index = [x[bit_index] for x in input_data]
    most_common_bit = get_most_common_bit(bits_at_index)
    
    # apply filter based on criterion
    if criterion == Criterion.MOST_COMMON:
        filtered_input_data = [x for x in input_data if x[bit_index] == most_common_bit]
    elif criterion == Criterion.LEAST_COMMON:
        filtered_input_data = [x for x in input_data if x[bit_index] != most_common_bit]

    return filtered_input_data

def calculate_rating(input_data: List[List[int]], rate: Rate):
    bit_index = 0
    while len(input_data) > 1:
        input_data = filter_by_criterion(input_data, bit_index, rate.value)
        bit_index += 1
    
    return bitlist_to_int(input_data[0])

def calculate_rates():
    raw_input_data = read_input()
    filtered_data = raw_input_data.copy()
    
    oxygen_generator_rating = calculate_rating(filtered_data, Rate.OXYGEN_GENERATOR)
    co2_scrubber_rating = calculate_rating(filtered_data, Rate.CO2_SCRUBBER)    
    
    print(f"Oxygen generator rating: {oxygen_generator_rating}")
    print(f"CO2 scrubber rating: {co2_scrubber_rating}")
    print(f"Life Support rating: {oxygen_generator_rating * co2_scrubber_rating}")
    
if __name__ == '__main__':
    calculate_rates()