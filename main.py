import random

# Game configuration constants
MAX_LINES = 3        # Maximum number of lines a player can bet on
MAX_BET = 100        # Maximum bet amount per line
MIN_BET = 1          # Minimum bet amount per line
ROWS = 3             # Number of rows in the slot machine
COLS = 3             # Number of columns in the slot machine

# Symbol frequency configuration - determines how often each symbol appears
symbol_count = {
    "A": 2,  # Symbol A appears 2 times (rarest)
    "B": 4,  # Symbol B appears 4 times
    "C": 6,  # Symbol C appears 6 times
    "D": 8   # Symbol D appears 8 times (most common)
}

# Symbol payout values - multiplier for winnings
symbol_value = {
    "A": 5,  # Symbol A pays 5x the bet (highest payout)
    "B": 4,  # Symbol B pays 4x the bet
    "C": 3,  # Symbol C pays 3x the bet
    "D": 2   # Symbol D pays 2x the bet (lowest payout)
}

def check_winnings(columns, lines, bet, values):
    """
    Check for winning combinations and calculate total winnings.
    
    Args:
        columns (list): The slot machine result as a list of columns
        lines (int): Number of lines the player bet on
        bet (int): Amount bet per line
        values (dict): Symbol payout values
    
    Returns:
        tuple: (total_winnings, list_of_winning_lines)
    """
    winnings = 0
    winning_lines = []
    
    # Check each line for winning combinations
    for line in range(lines):
        symbol = columns[0][line]  # Get the first symbol in the line
        
        # Check if all symbols in this line match
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break  # Symbols don't match, no win on this line
        else:
            # All symbols matched - calculate winnings
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # Store line number (1-indexed)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a random slot machine spin result.
    
    Args:
        rows (int): Number of rows in the slot machine
        cols (int): Number of columns in the slot machine
        symbols (dict): Symbol frequency configuration
    
    Returns:
        list: A list of columns, each containing symbols for that column
    """
    # Create a list of all available symbols based on their frequency
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):  # Fixed: was using incorrect syntax
            all_symbols.append(symbol)
    
    columns = []
    
    # Generate each column
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Create a copy of all symbols
        
        # Fill each row in this column
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)  # Remove to avoid duplicates in same spin
            column.append(value)
        
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    """
    Display the slot machine result in a formatted grid.
    
    Args:
        columns (list): The slot machine result as a list of columns
    """
    # Print each row
    for row in range(len(columns[0])):
        # Print each symbol in the row
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Add separator between columns
            else:
                print(column[row], end="")     # No separator after last column
        print()  # New line after each row

def deposit():
    """
    Get the initial deposit amount from the player.
    
    Returns:
        int: The deposit amount
    """
    while True:
        amount = input("What would you like to deposit? $")
        
        # Validate input is a positive number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def get_number_of_lines():
    """
    Get the number of lines the player wants to bet on.
    
    Returns:
        int: Number of lines to bet on (1-MAX_LINES)
    """
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        
        # Validate input is within valid range
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines

def get_bet():
    """
    Get the bet amount per line from the player.
    
    Returns:
        int: Bet amount per line (MIN_BET to MAX_BET)
    """
    while True:
        amount = input("What would you like to bet on each line? $")
        
        # Validate input is within valid betting range
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    
    return amount

def spin(balance):
    """
    Execute a single spin of the slot machine.
    
    Args:
        balance (int): Player's current balance
    
    Returns:
        int: Net change in balance (winnings - total_bet)
    """
    lines = get_number_of_lines()
    
    # Get bet amount and ensure player has sufficient balance
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    
    # Display betting information
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    # Generate and display slot machine result
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    # Calculate and display winnings
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    
    # Return net change in balance
    return winnings - total_bet

def main():
    """
    Main game loop - handles the overall game flow.
    """
    # Get initial deposit
    balance = deposit()
    
    # Main game loop
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        
        # Check if player wants to quit
        if answer == "q":
            break
        
        # Execute a spin and update balance
        balance += spin(balance)
    
    # Display final balance when quitting
    print(f"You left with ${balance}")

# Start the game if this script is run directly
if __name__ == "__main__":
    main()