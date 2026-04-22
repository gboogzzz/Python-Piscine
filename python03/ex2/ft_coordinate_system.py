import math


def parse_coordinates(coord_str: str) -> tuple:
    coord_list = coord_str.split(",")
    try:
        x = int(coord_list[0])
        y = int(coord_list[1])
        z = int(coord_list[2])
        print(f"Parsed position: {x, y, z}")
        return (x, y, z)
    except ValueError as e:
        print(f"Parsing invalid coordinates: {coord_str}")
        print(f"Error parsing coordinates: {e.args[0]}")
        print(f"Error details - Type: {type(e).__name__}, Args: ({e.args})\n")


def calculate_distance(p1: tuple, p2: tuple) -> None:
    dist = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)
    print(f"Distance between {p1} and {p2}: {dist:.2f}\n")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    pos = (10, 20, 5)
    orig = (0, 0, 0)
    print("Position created:", pos)
    calculate_distance(orig, pos)
    pos_str = "3,4,0"
    print(f"Parsing coordinates: {pos_str}")
    pos1 = parse_coordinates(pos_str)
    calculate_distance(orig, pos1)
    pos_error = "abc,def,ghi"
    parse_coordinates(pos_error)
    x, y, z = pos1
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
