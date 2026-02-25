import sys
import math

class SizeCoordinateError(Exception):
    pass

def parsing(coordinates: tuple) -> tuple:
    print(f"Parsing coordinates: {coordinates}")
    if len(coordinates) != 3:
        raise SizeCoordinateError(f"must contain 3 values (x, y, z). "
                              f"you have: {coordinates}.")
    for value in coordinates:
        if not isinstance(value, int):
            raise ValueError(f"invalid literal for int() with base 10: '{value}'")
    print("Good coordinates!\n")
    return coordinates

def ft_coordinate_system(place1: tuple, place2: tuple) -> int:
    x1, y1, z1 = place1
    x2, y2, z2 = place2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance

def main() -> None:
    print ("=== Game Coordinate System ===")
    try:
        zero = parsing((0, 0, 0))
        position = parsing((10, 20, 5))
        print(f"Position created: {position}")
        coordinate = ft_coordinate_system(zero, position)
        print(f"Distance between {zero} and {position}: {coordinate:.2f}")
    except (ValueError, SizeCoordinateError) as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type {type(e).__name__}, Args: (\"{e}\")")

    print("\nUnpackig demonstration:")
    print("Player at x=3, y=4, z=0")
    player = (3,4,0)
    x, y, z = player
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
