import sys

def ft_command_quest() -> None:
    ac = len(sys.argv)
    prog_name = sys.argv[0]
    if ac == 1:
        print("No arguments provided!")
        print(f"Program name: {prog_name}")
        print(f"Total arguments: {ac}")
    else:
        print(f"Program name: {prog_name}")
        print(f"Arguments received: {ac - 1}")
        i = 1
        while i < ac:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {ac}")

if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest()
