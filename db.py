def read_money():
    try:
        money_list = []
        with open("money.txt", "r") as file:
            for line in file:
                line = line.replace("\n", "")
                money_list.append(line)
        return money_list
    except FileNotFoundError:
        print()
        print("Could not find items file!")
        print("Exiting program.  Bye!")


def write_money(money):
    with open('money.txt', 'w') as f:
        f.write(str(money))

        #with open(INVENTORY_FILENAME, "w") as file:
        #    for item in inventory:
        #        file.write(item + "\n")