from dataclasses import dataclass
import dataclasses
from enum import Enum
import pathlib
from typing import Tuple

FILE_PATH = pathlib.Path(__file__).parent / "input_files" / "input.txt"

### utils ###

def multiply_tuple_by_scalar(t: Tuple[int, int], s: int):
    return (t[0] * s, t[1] * s)

def add_tuples(t1: Tuple[int, int], t2: Tuple[int, int]):
    return (t1[0] + t2[0], t1[1] + t2[1])

### classes ###

class Direction(Enum):
    FORWARD = (1, 0)
    DOWN = (0, 1)
    UP = (0, -1)
    
PILOT_COMMANDS = {
    "forward": Direction.FORWARD,
    "down": Direction.DOWN,
    "up": Direction.UP
}

@dataclass
class InputCommand:
    direction: Direction
    distance: int
    
    @staticmethod
    def from_raw_command_str(raw_command: str):
        splitted_command = raw_command.split(" ")
        return InputCommand(
            direction=PILOT_COMMANDS[splitted_command[0]],
            distance=int(splitted_command[1])
        )

@dataclass
class Position:
    coordinates: Tuple[int, int] = (0, 0)
    
    def apply_command(self, command: InputCommand):
        movement = multiply_tuple_by_scalar(command.direction.value, command.distance)
        self.coordinates = add_tuples(self.coordinates, movement)

def parse_commands():
    with open(FILE_PATH, 'r') as f:
        raw_pilot_commands = f.read().splitlines()
        return [InputCommand.from_raw_command_str(raw_command) for raw_command in raw_pilot_commands]
    
def calculate_position():
    curr_position = Position()
    commands = parse_commands()
    
    for command in commands:
        curr_position.apply_command(command)
        
    print(curr_position.coordinates)
    print(curr_position.coordinates[0] * curr_position.coordinates[1])
        
if __name__ == '__main__':
    calculate_position()