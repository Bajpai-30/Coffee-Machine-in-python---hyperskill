amount = 550
water = 1200
milk = 540
coffee = 120
cups = 9


def print_state():
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{coffee} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{amount} of money')
    print()


def select_action() -> str:
    return input('Write action (buy, fill, take): ')


def select_flavor() -> int:
    return int(input('What do you want to buy?'
                     ' 1 - espresso, 2 - latte, 3 - cappuccino: '))


def buy():
    global amount, water, milk, beans, cups

    flavor = select_flavor()
    if flavor == 1:  # espresso
        assert water >= 250
        assert coffee >= 16

        money += 4
        water -= 250
        coffee -= 16
    elif flavor == 2:  # latte
        assert water >= 350
        assert milk >= 75
        assert coffee >= 20

        amount += 7
        water -= 350
        milk -= 75
        coffee -= 20
    elif flavor == 3:  # cappuccino
        assert water >= 200
        assert milk >= 100
        assert coffee >= 12

        amount += 6
        water -= 200
        milk -= 100
        coffee -= 12
    else:
        raise ValueError(f'Unknown flavor {flavor}')

    cups -= 1


def fill():
    global water, milk, coffee, cups

    water += int(input('how many ml of water do you want to add: '))
    milk += int(input('how many ml of milk do you want to add: '))
    coffee += int(input('how many grams of coffee'
                       ' do you want to add: '))
    cups += int(input('how many disposable cups of coffee'
                      ' do you want to add: '))


def take():
    global amount

    print(f'I gave you ${amount}')
    money = 0


def main():
    print_state()

    action = select_action()

    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    else:
        raise ValueError(f'Unknown command {action}')

    print()
    print_state()


if __name__ == '__main__':
    main()