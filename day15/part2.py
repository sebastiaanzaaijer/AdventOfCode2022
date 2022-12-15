from collections import namedtuple, defaultdict

Point = namedtuple("Point", "x y")
SensorBeaconPair = namedtuple("SensorBeaconPair", "sensor beacon")

def manhattan_radius(sensor_beacon_pair):
    return ( 
        abs(sensor_beacon_pair.sensor.x - sensor_beacon_pair.beacon.x) +
        abs(sensor_beacon_pair.sensor.y - sensor_beacon_pair.beacon.y)
    )

def create_sensor_beacon_pair(line):
    s,b = line.split(":")
    s = Point(*map(int,((_.split("=")[-1]) for _ in s.split(", ")[-2:])))
    b = Point(*map(int,((_.split("=")[-1]) for _ in b.split(", ")[-2:])))
    return SensorBeaconPair(s,b)

def range_on_row(sensor_beacon_pair,row):
    r = manhattan_radius(sensor_beacon_pair)
    s = sensor_beacon_pair.sensor
    if row < s.y-r or row > s.y+r:
        return None
    else:
        v_offset = abs(s.y-row)
        h_range = r-v_offset
        return [s.x-h_range,s.x+h_range]

def merge_ranges(ranges):
    new_ranges = []
    for range_ in sorted(ranges, key=lambda _: _[0]):
        if len(new_ranges) == 0:
            new_ranges.append(range_)
        else:
            if new_ranges[-1][1]+1 >= range_[0]:
                new_ranges[-1][1] = max(range_[1],new_ranges[-1][1])
            else:
                new_ranges.append(range_)
    return new_ranges

def solve_puzzle(puzzle_input,maxrows=4_000_000):
    sensor_beacon_pairs = [create_sensor_beacon_pair(_) for _ in puzzle_input.splitlines()]
    for row in range(maxrows):
        ranges = []
        for sensor_beacon_pair in sensor_beacon_pairs:
            range_ = range_on_row(sensor_beacon_pair,row)
            if range_:
                ranges.append(range_)
        ranges = merge_ranges(ranges)
        if len(ranges)==2:
            return 4000000*(ranges[0][1]+1)+row

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))