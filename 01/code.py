import pathlib

FILE_PATH = pathlib.Path(__file__).parent / "input_files" / "input.txt"
WINDOW_SIZE = 3

def parse_readings():
    with open(FILE_PATH, 'r') as f:
        depth_readings = [int(d.rstrip()) for d in f.readlines()]
        return depth_readings

def single_step_increases():
    depth_readings = parse_readings()
    
    depth_increases = 0
    last_depth_measurement = None
    for depth in depth_readings:
        if last_depth_measurement is not None and depth > last_depth_measurement:
            depth_increases += 1
        last_depth_measurement = depth

    print(depth_increases)
    
def windowed_increases():
    depth_readings = parse_readings()
    
    windowed_depth_increases = 0
    for i in range(WINDOW_SIZE, len(depth_readings)):
        window_diff = depth_readings[i] - depth_readings[i - WINDOW_SIZE]
        if window_diff > 0:
            windowed_depth_increases += 1
            
    print(windowed_depth_increases)
        
if __name__ == '__main__':
    # single_step_increases()
    windowed_increases()    