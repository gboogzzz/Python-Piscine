def ft_count_harvest_recursive():
    def helper(n, actual):
        if actual > n:
            return
        print(f"Day {actual}")
        helper(n, actual + 1)
    n = int(input("Days until harvest: "))
    helper(n, 1)
    print("Harvest time!")
