# Slot Machine Game

A simple command-line slot machine game written in Python. Players can deposit money, place bets on multiple lines, and spin the reels to try their luck!

## Features

- **Multi-line betting**: Bet on 1-3 lines simultaneously
- **Flexible betting amounts**: Choose your bet per line ($1-$100)
- **Symbol-based payouts**: Different symbols have different rarity and payout values
- **Balance tracking**: Keep track of your winnings and losses
- **Input validation**: Robust error handling for user inputs

## Game Rules

### Symbols and Payouts

The slot machine uses 4 different symbols with varying rarity and payout multipliers:

| Symbol | Frequency | Payout Multiplier | Rarity |
|--------|-----------|-------------------|---------|
| A      | 2/20      | 5x               | Rarest |
| B      | 4/20      | 4x               | Rare |
| C      | 6/20      | 3x               | Common |
| D      | 8/20      | 2x               | Most Common |

### Winning Conditions

- To win on a line, all 3 symbols in that line must match
- You can bet on 1, 2, or 3 lines
- Winnings = Symbol multiplier × Bet per line
- Total payout is calculated for all winning lines

### Betting Limits

- **Minimum bet per line**: $1
- **Maximum bet per line**: $100
- **Maximum lines**: 3
- **Slot machine size**: 3×3 grid

## Installation

1. Make sure you have Python 3.x installed on your system
2. Download the `slot_machine.py` file
3. No additional dependencies required (uses only built-in Python modules)

## How to Run

```bash
python slot_machine.py
```

## How to Play

1. **Start the game**: Run the Python script
2. **Make a deposit**: Enter the amount you want to start with
3. **Choose number of lines**: Select 1-3 lines to bet on
4. **Place your bet**: Choose how much to bet per line
5. **Spin the reels**: Press Enter to spin (or 'q' to quit)
6. **Check results**: See if you won on any lines
7. **Continue playing**: Your balance updates automatically

## Example Gameplay

```
What would you like to deposit? $100
Current balance is $100
Press enter to play (q to quit).
Enter the number of lines to bet on (1-3)? 2
What would you like to bet on each line? $10
You are betting $10 on 2 lines. Total bet is equal to: $20

A | B | C
D | D | D
C | A | B

You won $20.
You won on lines: 2
Current balance is $100
```

## Code Structure

### Main Functions

- **`main()`**: Main game loop and flow control
- **`deposit()`**: Handles initial deposit input
- **`spin(balance)`**: Executes a single spin
- **`get_number_of_lines()`**: Gets line selection from player
- **`get_bet()`**: Gets bet amount from player
- **`get_slot_machine_spin()`**: Generates random slot results
- **`print_slot_machine()`**: Displays the slot machine grid
- **`check_winnings()`**: Calculates winnings and winning lines

### Configuration

Game settings can be easily modified by changing the constants at the top of the file:

```python
MAX_LINES = 3        # Maximum lines to bet on
MAX_BET = 100        # Maximum bet per line
MIN_BET = 1          # Minimum bet per line
ROWS = 3             # Slot machine rows
COLS = 3             # Slot machine columns
```

Symbol frequencies and payouts can be adjusted in the dictionaries:

```python
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}  # Frequency
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}  # Payout multipliers
```

## Technical Details

- **Language**: Python 3.x
- **Dependencies**: None (uses only built-in modules)
- **Input validation**: Comprehensive error checking for all user inputs
- **Randomization**: Uses Python's `random` module for fair slot generation
- **Memory management**: Symbols are removed from the pool during each spin to prevent duplicates

## Potential Enhancements

- Add sound effects
- Implement progressive jackpots
- Add more symbol types
- Create a GUI version
- Add player statistics tracking
- Implement save/load functionality for balance
- Add bonus rounds or special features
