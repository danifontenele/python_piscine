def garden_operations():
    data_dict = {"rose": 20}
    return data_dict


def test_error_types(file: str) -> None:
    data_dict = garden_operations()
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        int("vinte e dois")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        open(file)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: no such file {file}\n")

    print("Testing KeyError...")
    try:
        data_dict["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")

    print("Testing multiple errors together...")
    try:
        int("forty two")
        42 / 0
        data_dict["missing_plant"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types("test.txt")
