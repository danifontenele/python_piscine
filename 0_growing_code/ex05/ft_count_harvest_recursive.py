def ft_count_harvest_recursive(d=None):
    if d is None:
        d = int(input("Days until harvest: "))
        ft_count_harvest_recursive(d)
        print("Harvest time!")
        return
    if d <= 0:
        return
    ft_count_harvest_recursive(d - 1)
    print(f"Day {d}")


ft_count_harvest_recursive()
