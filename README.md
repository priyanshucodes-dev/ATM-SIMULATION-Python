# ATM-SIMULATION-Python
🏧 A Python-based ATM Simulation system featuring PIN authentication, balance checking, deposits, withdrawals, cash denomination management, and mini statements using core Python concepts.
🏧 ATM Simulation System Using Python

A simple, menu-driven ATM Simulation System built using Python. This project simulates basic ATM operations, including user authentication, balance inquiry, cash deposits, withdrawals, and mini statements.

The system also manages ATM cash availability using different currency denominations and maintains a transaction history for each account.

✨ Features
🔐 PIN Authentication: Secure account access using an account number and PIN.
🔢 Limited Login Attempts: Allows up to three incorrect PIN attempts before blocking access for the current session.
💰 Check Balance: View the current account balance.
📥 Cash Deposit: Deposit money into an account and update the balance.
📤 Cash Withdrawal: Withdraw money after checking account balance and ATM cash availability.
💵 Denomination Management: Dispenses cash using ₹500, ₹200, ₹100, and ₹50 notes.
🧾 Mini Statement: View the last five transactions, including transaction type, amount, and balance after each transaction.
🏦 Multiple Accounts: Supports multiple predefined bank accounts.
✅ Input Validation: Checks withdrawal and deposit amounts to ensure they are valid positive numbers.
🚪 Exit Option: Safely exit the ATM system.
🛠️ Technologies Used
Programming Language: Python 3
Concepts Used:
Variables and data types
Dictionaries and lists
Functions
Conditional statements (if, elif, else)
Loops (while and for)
User input and validation
Basic transaction history management
Arithmetic operations
📂 Project Structure
ATM-Simulation-Python/
│
├── atm.py
└── README.md

Note: atm.py is the suggested Python filename. Replace it with your actual filename if it is different.
⚙️ How to Run the Project
Prerequisites

Make sure Python 3 is installed on your computer.

Step 1: Clone the Repository
git clone YOUR_REPOSITORY_URL


Replace YOUR_REPOSITORY_URL with your GitHub repository's clone URL.

Step 2: Navigate to the Project Folder
cd ATM-Simulation-Python

Step 3: Run the Program
python atm.py


Depending on your system, you may need to use:

python3 atm.py

👤 Sample Login Accounts

The program currently contains two predefined accounts.

Account Number	Account Holder	PIN	Initial Balance
1001	Sahejveer	1232	₹74,000
1002	Priyanshu	1980	₹50,000

Important: These are sample credentials defined in the source code for demonstration purposes. Do not use real banking credentials.

🖥️ How It Works
1. Login

The user enters an account number and PIN. If the credentials are correct, access to the ATM menu is granted.

2. Check Balance

Displays the current balance of the logged-in account.

3. Deposit

Accepts a positive deposit amount, updates the account balance, and records the transaction in the account's history.

4. Withdraw

Checks whether:

The requested amount is valid.
The account has sufficient funds.
The amount is a multiple of ₹50.
The ATM has enough notes to dispense the requested amount.

If all checks pass, the system dispenses the available denominations, deducts the amount from the account balance, and records the transaction.

5. Mini Statement

Displays the last five transactions, including:

Transaction type
Transaction amount
Balance after the transaction
6. Exit

Ends the current ATM session.

💵 ATM Cash Management

The ATM supports the following denominations:

Note Denomination	Initial Number of Notes
₹500	20
₹200	30
₹100	50
₹50	100

The program uses a greedy approach to select notes, starting with the highest denomination and moving to the lowest. It also checks the available note count before dispensing cash.

📚 Learning Objectives

This project helped me practice and understand:

Writing modular Python programs using functions.
Managing account information using dictionaries.
Storing transaction records using lists and tuples.
Validating user input.
Implementing PIN-based login logic.
Using loops and conditional statements to control program flow.
Simulating cash withdrawal with limited currency denominations.
Updating account balances and maintaining transaction histories.
🚀 Future Improvements

Possible enhancements for future versions include:

Add account creation functionality.
Store account information and transaction history in a file or database.
Add fund transfers between accounts.
Add daily withdrawal limits.
Improve withdrawal logic to find a valid combination of notes when the greedy approach fails.
Add transaction dates and timestamps.
Introduce a graphical user interface (GUI).
Add automated tests for deposits, withdrawals, and ATM cash management.
Implement stronger authentication and secure PIN storage.
⚠️ Limitations
Account details are predefined in the Python source code.
Account balances and transaction histories are not saved permanently.
PINs are stored directly in the code and are not encrypted or hashed.
Login blocking applies only to the current program session.
The withdrawal algorithm uses a greedy approach, which may reject an amount even when another valid combination of available notes exists.

Disclaimer: This project is intended for educational purposes only. It is a basic ATM simulation and is not suitable for real banking or financial transactions.

👨‍💻 Author

Priyanshu

📄 License

This project is available for educational and learning purposes. 
