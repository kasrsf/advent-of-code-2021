import pathlib
from typing import List

FILE_PATH = pathlib.Path(__file__).parent / "input_files" / "input.txt"
DAYS_UNTIL_NEW_FISH = 6
NEW_FISH_DELAY = 2
NEW_FISH_DAYS_UNTIL_NEW_FISH = DAYS_UNTIL_NEW_FISH + NEW_FISH_DELAY

def unsigned_elementwise_not(x: int, size: int) -> int:
    mask = int('1' * size, 2)
    return mask ^ x

def read_input():
    with open(FILE_PATH, 'r') as f:
        raw_inputs = f.read().splitlines()[0]
        initial_state = [int(x) for x in raw_inputs.split(',')]
        
        return initial_state
    
def step(curr_state: List[int]):
    return [x - 1 for x in curr_state]

def calculate_state(days: int, verbose: bool = False):
    curr_state = read_input()
    remaining_days = days
    while remaining_days > 0:
        curr_state = step(curr_state)
        
        for ix, lantern_fish_age in enumerate(curr_state):
            if lantern_fish_age < 0:
                # generate new fish and reset age
                curr_state[ix] = DAYS_UNTIL_NEW_FISH
                curr_state.append(NEW_FISH_DAYS_UNTIL_NEW_FISH)
        
        if verbose is True:
            print(f"After {days - remaining_days + 1} days: {curr_state}")
        remaining_days -= 1
    
    print(f"Number of Fish: {len(curr_state)}")
    
if __name__ == '__main__':
    calculate_state(days=80)