import math


def ft_coordinate_system(args: str) -> tuple[int, int, int] | None:
    try:
        lst = []
        splited = args.split(",")
        for i in splited:
            lst.append(int(i))
        if len(lst) != 3:
            raise ValueError("Need 3 coordinates exactly")
        return tuple(lst)
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{args}"')
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
        return None


def calculate_cordinates(tup: tuple[int, int, int]) -> None:
    x2, y2, z2 = tup
    x1, y1, z1 = (0, 0, 0)
    res = int(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) * 100) / 100
    print(
        f"Distance between ({x1}, {y1}, {z1}) and {tup}: {res}\n"
    )


def display_coordinates(args: str) -> None:
    lst = ft_coordinate_system(args)
    if lst is None:
        return
    print(f'Parsing coordinates: "{args}"')
    print(f"Parsed position: {lst}")
    calculate_cordinates(lst)


def unpacking(args: str) -> None:
    tup = ft_coordinate_system(args)
    if tup is None:
        return
    x, y, z = tup
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":

    print("=== Game Coordinate System ===\n")
    arg = ft_coordinate_system("10,20,5")
    print(f"Position created: {arg}")

    calculate_cordinates(arg)

    display_coordinates("3,4,0")

    display_coordinates("abc,def,ghi")

    unpacking("3,4,0")
