import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,         # means if A comes in the spin, your bet is multiplied by 5 times and so on.....
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):        # (line means row), (values = symbol_value)
    winnings = 0
    winning_line = []

    for line in range(lines):       # looping through every row
        symbol = columns[0][line]       # it gives the symbol which is at the first column of a particular line/row
        for column in columns:      # looping through every column to check that symbol
            symbol_to_check = column[line]      # symbol_to_check checks the symbol at the column of the current row
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet        # values[symbol] = symbol_value
            winning_line.append(line + 1)   # gives the line on which the condition is true ie.user won (x + 1 coz line index starts from 0)

    return winnings, winning_line        


def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():     # .items() gives both the key as well as the value 
        for _ in range(symbol_count):
            all_symbols.append(symbol)      # therefore, A will be added 2 times, B will be added 4 times, C will be added 6 times, D will be added 8 times in the list

    columns = []      
    for _ in range(cols):   # this will be done for each column
        column = []
        current_symbols = all_symbols[:]    # means current_symbols is a copy of all_symbols
        for _ in range(rows):     # for every column we will generate some number of values ie. no of rows
            value = random.choice(current_symbols)   # we will choose random values from the COPY and not the og list bcoz once we remove particular value from the list we cannot choose it again   
            current_symbols.remove(value)     # it will find first instance of that value in the list and remove it from the list so that we don't pick it again
            column.append(value)

# after this, jitne bhi rows/sybmols are there in the column, we now add it to the columns list
        columns.append(column) 

    return columns       


def print_slot_machine(columns):
# [A, B, C]  =>  [A] [.] [.]
# [...]          [B] [.] [.]
# [...]          [C] [.] [.]
                
    for row in range(len(columns[0])):   # no of rows = number of elements in the columns list ie. its length ([0] assumes there is atleast one column in the list)
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:   # if i = len(columns) - 1, ie.if it is at the last element in the column, then do not print |, just print the element at that position only
                print(column[row], end=" ")

        print()     # prints new line after each row


def deposit():
    while True:
        amount = int(input("How much would you like to deposit? Rs."))
        if amount > 0:
            break
        else:
            print("Amount must be greater than zero")
    return amount       # will be called from main func


def get_no_of_lines():
    while True:
        lines = int(input(f"Enter number of lines to bet on (1 - {MAX_LINES}): "))
        if 1 <= lines <= MAX_LINES:
            break
        else:
            print("Enter valid number of lines")
    return lines        # will be called from main func


def get_bet():
    while True:
        bet = int(input("How much would you like to bet on each line? Rs."))
        if MIN_BET <= bet <= MAX_BET:
            break
        else:
            print(f"Amount must be between Rs.{MIN_BET} - Rs.{MAX_BET}")
    return bet  


def spin(balance):
    lines = get_no_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet that much. Current bal = Rs.{balance}")
        else:
            break    

    print(f"You are betting Rs.{bet} on {lines} lines. Total bet is equal to: Rs.{total_bet}")

    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won Rs.{winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()         # deposit returns amount deposited
    while True:
        print(f"Current balance is Rs.{balance}")
        answer = input("Press enter to play (q to quit).")
        if spin == "q":
            break
        balance += spin(balance)       # spin(balance) returns return winnings - total_bet ie. current balance

    print(f"You left with Rs.{balance}")    
    
main()     