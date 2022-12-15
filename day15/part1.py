from collections import namedtuple

Point = namedtuple("Point", "x y")
SensorBeaconPair = namedtuple("SensorBeaconPair", "sensor beacon")

def print_sensor_range(sensor_beacon_pair):
    r = manhattan_radius(sensor_beacon_pair)
    s = sensor_beacon_pair.sensor
    for y in range(s.y-r-3,s.y+r+1+3):
        points = points_on_row(sensor_beacon_pair,y)
        for x in range(s.x-r-3,s.x+r+1+3):
            print("#" if Point(x,y) in points else ".",end="")
        print()


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

def points_on_row(sensor_beacon_pair,row):
    r = manhattan_radius(sensor_beacon_pair)
    s = sensor_beacon_pair.sensor
    if row < s.y-r or row > s.y+r:
        return set()
    else:
        v_offset = abs(s.y-row)
        h_range = r-v_offset
        return set(Point(x,row) for x in range(s.x-h_range,s.x+h_range+1))

def solve_puzzle(puzzle_input,row=2000000):
    sensor_beacon_pairs = [create_sensor_beacon_pair(_) for _ in puzzle_input.splitlines()]
    beacons = set(_.beacon for _ in sensor_beacon_pairs)
    points = set()
    for sensor_beacon_pair in sensor_beacon_pairs:
        points = points.union(points_on_row(sensor_beacon_pair,row))
    points -= beacons
    return len(points)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))