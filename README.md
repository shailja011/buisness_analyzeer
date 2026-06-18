 # Business Analyzer Pipeline 

Welcome to my project! I built this minor project to solve a common problem that startup founders face: trying to keep track of daily business data without drowning in disorganized spreadsheets or overly complicated software. 

This platform serves as a central cockpit for a founder, instantly reading raw data from different parts of a company and pulling it together into a single, clean dashboard.


 Why I Built It This Way (The Architecture)

When I started writing Python, it was easy to put all my code into one massive script. But as a project grows, that approach completely falls apart. To challenge myself, I built this using a **modular, decoupled package architecture**. 

By breaking the code into independent sub-packages, each piece of the application has one clear job:
* **`main.py`** - The main switchboard. It handles the core flow of the program and starts the dashboard.
* **`database/`** - Where our raw data lives safely inside flat `.csv` sheets (`finances.csv`, `employees.csv`, `inventory.csv`).
* **`financial_manager/`** - The finance brain. It reads numbers and handles all the core financial calculations.
* **`resource_manager/`** - Keeps track of physical assets, quantities, and company equipment valuations.
* **`employess/`** - Manages team payroll data and workforce metrics.
* **`executive_insights/`** - The final presentation layer. It takes all the raw math and prints out clean insights for the founder.



# Key Lessons & Engineering Features

Building this project taught me a lot about writing production-grade software. Here are the core features I'm most proud of implementing:

* **Separation of Concerns:** The database, the calculation engines, and the final display code are completely isolated from one another. This means I can update the finance math without breaking how the inventory package works.
* **Defensive Error Handling:** I wrapped our data parsing layers in defensive `try-except` blocks. If a spreadsheet goes missing or someone types text where a number should be, the application won't crash—it handles the problem gracefully.
* **Automated Audit Logging:** I built a custom background logging engine. Whenever a system fault or data corruption happens, it automatically writes a permanent, date-stamped note inside a `logs/errors.txt` file so developers can audit the issue later.
* **Real Venture Metrics:** Instead of basic addition, the pipeline computes actual business-critical health indicators like monthly burn rate, customer acquisition costs, and cash runway months.



# Technologies Used    
* **Language:** Python 3.x
* **Core Modules:** `os`, `csv`, `datetime`
* **Data Storage:** Flat CSV Storage Arrays
