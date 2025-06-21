# 🎰 Slot Machine Game (Python CLI)

This is a terminal-based slot machine game written in Python. Players can deposit money, bet on up to 3 lines, spin the slot machine, and win money based on matching symbols.

---

## 🚀 Features

- Deposit and manage a virtual balance  
- Bet on 1 to 3 lines per spin  
- Randomized slot results with varying symbol frequencies  
- Winnings based on symbol value and matched lines  
- Input validation to prevent invalid bets or over-betting

---

## 🧠 Python Concepts Used

- Functions and loops  
- Dictionaries and lists  
- Random number generation (`random`)  
- Input validation and error handling  
- Basic game state logic

---

## 🕹️ How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. Enter a deposit amount.
3. Choose how many lines to bet on (1–3).
4. Enter a bet amount per line.
5. Spin to see if you win. Your balance updates automatically.

---

## 💰 Symbol Details

| Symbol | Frequency | Payout Multiplier |
| ------ | --------- | ----------------- |
| A      | 2         | 5× bet            |
| B      | 4         | 4× bet            |
| C      | 6         | 3× bet            |
| D      | 8         | 2× bet            |

A line wins if all symbols on that horizontal row match across columns.

---

## 📄 File

* `main.py`: Contains all game logic and runs the interactive CLI slot machine.
