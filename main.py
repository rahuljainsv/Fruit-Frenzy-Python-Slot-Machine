import random

MAX_LINES = 3  # 1 is top line, 2 is top and middle line , 3 is all three lines
MAX_BET = 10000
MIN_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "🥭": 2,
    "🍎": 4,
    "🍍": 6,
    "🍌": 8,
}

symbol_value = {
    "🥭": 5,
    "🍎": 4,
    "🍍": 3,
    "🍌": 2,
}


def spin(balance_amount):
    while True:
        lines = ip_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance_amount:
            print(f"Not enough balance to bet on, current balance is ₹{balance_amount} bet is ₹{total_bet}.")
            print("Choose appropriate number of lines and betting amount.")
        else:
            break
    print(f"Betting ₹{bet} on {lines} lines. Total bet is ₹{total_bet}.\n")
    print("Fruit Frenzy")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"\nYou won ₹{winnings}")
    print(f"You won on lines: ", *winning_lines) # splat operator (passes every single value)
    return winnings - total_bet


def main():
    print("\nWelcome to Little Slots of Fun Casino\n")
    print("Friut Frency \n(minimum bet is 100 and in multiples of x1)\n")
    balance_amount = deposit()
    while True:
        print(f"Current balance is ₹{balance_amount}\n")
        answer = input("Press enter to play, q to quit.\n")
        if answer == "q":
            print(f"\nWithdrawable amount = ₹{balance_amount}")
            print("Would love to see you around again soon.")
            break
        elif balance_amount < 100:
            print("Insufficient balance to spin again.\nRestart with new deposit to play again.")
            break
        balance_amount += spin(balance_amount)

    print("Little Slots of Fun Casino inc.\n")


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):  # _ anonymous variable, iteration value is not required
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # copying with [:] (= is pass by reference)
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    # transposing the spin for printing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row])


def ip_number_of_lines():
    while True:
        lines = input("Number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Not a valid number of lines")
    return lines


def get_bet():
    while True:
        bet = input("Bet amount (for each line): ₹")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET} - ₹{MAX_BET}")
    return bet


def deposit():
    while True:
        amount = input("Deposit amount: ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 100:
                break
            else:
                print("Deposit amount below minimum bet of ₹100")
        else:
            print("Not a valid amount")
    return amount


main()