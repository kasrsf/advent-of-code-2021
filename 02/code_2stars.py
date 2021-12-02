from dataclasses import dataclass
import pathlib

FILE_PATH = pathlib.Path(__file__).parent / "input_files" / "input.txt"

@dataclass
class State:
    x: int = 0
    y: int = 0
    aim: int = 0

class Direction:
    @staticmethod
    def forward(state: State, amount: int):
        state.x += amount
        state.y += state.aim * amount
    
    @staticmethod
    def down(state: State, amount: int):
        state.aim += amount
        
    @staticmethod
    def up(state: State, amount: int):
        state.aim -= amount
    
PILOT_COMMANDS = {
    "forward": Direction.forward,
    "down": Direction.down,
    "up": Direction.up
}

@dataclass
class InputCommand:
    direction: Direction
    amount: int
    
    @staticmethod
    def from_raw_command_str(raw_command: str):
        splitted_command = raw_command.split(" ")
        return InputCommand(
            direction=PILOT_COMMANDS[splitted_command[0]],
            amount=int(splitted_command[1])
        )
    
    def apply_to_state(self, state: State):
        self.direction(state, self.amount)

@dataclass
class Position:
    state: State = State()
    
    def apply_command(self, command: InputCommand):
        command.apply_to_state(self.state)

def parse_commands():
    with open(FILE_PATH, 'r') as f:
        raw_pilot_commands = f.read().splitlines()
        return [InputCommand.from_raw_command_str(raw_command) for raw_command in raw_pilot_commands]
    
def calculate_position():
    curr_position = Position()
    commands = parse_commands()
    
    for command in commands:
        curr_position.apply_command(command)
        
    print(curr_position.state)
    print(curr_position.state.x * curr_position.state.y)
        
if __name__ == '__main__':
    calculate_position()