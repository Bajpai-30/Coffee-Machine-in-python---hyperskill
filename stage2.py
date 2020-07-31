def main():
    cups = int(input('How many cups of coffee you will need: '))

    # 1 cup: 200 ml of water, 50 ml of milk, and 15 g of Coffee Beans
    water = 200 * cups
    milk = 50 * cups
    Coffee = 15 * cups

    print(f'For {cups} cups of coffee you will need:')
    print(f'{water} ml of water')
    print(f'{milk} ml of milk')
    print(f'{Coffee} g of coffee beans')


if __name__ == '__main__':
    main()