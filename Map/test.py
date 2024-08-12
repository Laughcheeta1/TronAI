from Map import TronMap


def main():
    tron = TronMap()
    tron.print_map()

    while not tron.game_finished():
        print(tron.get_available_moves())
        x = int(input("Enter X coordinate: "))
        y = int(input("Enter Y coordinate: "))

        result = tron.add_move(x, y)
        print(result)
        tron.print_map()
        print(f"The amount of reachable space 1 has is: {tron.count_reachable_spaces(1)}")


if __name__ == '__main__':
    main()
