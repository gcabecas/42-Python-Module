def ft_count_harvest_recursive(days_until=0, first_day=0):
    if first_day == 0:
        days_until = int(input("Days until harvest: "))
        first_day += 1
    print(f"Day {first_day}")
    if days_until > first_day:
        ft_count_harvest_recursive(days_until, first_day + 1)
    if first_day == days_until:
        print("Harvest time!")
    elif days_until == 0:
        print("Harvest time!")
