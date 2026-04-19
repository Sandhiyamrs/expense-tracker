# 💰 Expense Tracker CLI

## 📌 Problem Statement
Many people fail to track their daily expenses, which leads to poor financial management.  
This project solves that problem by providing a simple command-line tool to record and analyze expenses.

---

## 🎯 Features
- Add new expense (amount, category, note, date)
- View all expenses
- Filter expenses by category
- Calculate total spending
- Persistent data storage using JSON

---

## 🛠️ Tech Stack
- Python (Core)
- JSON (for data storage)
- CLI (Command Line Interface)

---

## 📁 Project Structure

expense-tracker-cli/

│── main.py # Main application (CLI + menu)

│── expense.py # Expense class (data model)

│── storage.py # JSON read/write operations

│── utils.py # Helper functions

│── data/

│ └── expenses.json # Stored data

│── README.md

│── requirements.txt


---

## ▶️ How to Run

1. Clone the repository:
    git clone https://github.com/sandhiyamrs/expense-tracker.git
cd expense-tracker-cli


2. Run the program:
   python main.py


---

## 📸 Sample Output
==== Expense Tracker ====

Add Expense
View Expenses
Filter by Category
Show Total Spending
Exit
   
   
---

## 🧠 Concepts Used
- Object-Oriented Programming (OOP)
- File Handling (JSON)
- Modular Programming
- CLI-based Interaction

---

## 🚀 Future Improvements
- Add delete/update expense feature
- Assign unique IDs to each expense
- Monthly/weekly reports
- Convert to GUI or Web App

---

## 👤 Author
Sandhiya M
GitHub: https://github.com/sandhiyamrs
