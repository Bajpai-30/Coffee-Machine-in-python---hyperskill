def count(water: int, milk: int, beans: int, cups: int) -> str:
    n = min([
        water // 200,
        milk // 50,
        coffee // 15
    ])

    if n == cups:
        message = 'Yes, I can make that amount of coffee'
    elif n > cups:
        message = f'Yes, I can make that amount of coffee' \
                  f' (and even {n- cups} more than that)'
    else:
        message = f'No, I can make only {n} cups of coffee'

    return message


def main():
    water = int(input('how many ml of water the coffee machine has: '))
    milk = int(input('how many ml of milk the coffee machine has: '))
    coffee = int(input('how many grams of coffee beans'
                      ' the coffee machine has: '))
    cups = int(input('how many cups of coffee you will need: '))

    print(count(water, milk, coffee, cups))


if __name__ == '__main__':
    main()