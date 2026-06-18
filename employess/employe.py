import csv
import os
from executive_insights.logger import log_error

def salary_insights(filepath="database/employees.csv"):
    if not os.path.exists(filepath):
        err = "the file does not exist at specified path"
        log_error("employess", err)
        return {"error": err}
        
    employees = {}
    Total_salary_spent = 0
    
    try:
        with open(filepath, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees[row['name']] = int(row['monthly_salary'])
                Total_salary_spent += int(row['monthly_salary'])
    except (ValueError, KeyError) as e:
        err = f"Data corruption or missing column in employees.csv ({str(e)})"
        log_error("employess", err)
        return {"error": err}
            
    return {
        "Total salary of all employees": Total_salary_spent
    }
