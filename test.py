from Map import TronMap


def main():
    tron = TronMap()
    tron.print_map()

    while not tron.game_finished():
        x = int(input("Enter X coordinate: "))
        y = int(input("Enter Y coordinate: "))

        print(tron.get_available_moves())
        result = tron.add_move(x, y)
        print(result)
        tron.print_map()



if __name__ == '__main__':
    main()
