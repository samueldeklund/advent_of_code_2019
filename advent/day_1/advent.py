def calc_mass(mass):
    return mass // 3 - 2


def calc_total_fuel(mass):
    total_fuel = 0
    fuel = calc_mass(mass)
    while fuel > 0:
        total_fuel += fuel
        fuel = calc_mass(fuel)
    return total_fuel


def calc_ans(func, data):
    return sum(map(func, data))


def main():
    with open("./input.txt") as file:
        data = list(map(int, file.readlines()))
    print(f"Part One: {calc_ans(calc_mass, data)}")
    print(f"Part Two: {calc_ans(calc_total_fuel, data)}")


if __name__ == "__main__":
    main()
