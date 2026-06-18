import csv
import os
from executive_insights.logger import log_error

def inventory_assets(filepath="database/inventory.csv"):
    if not os.path.exists(filepath):
        err = "inventory.csv file not found at specified path"
        log_error("resource_manager", err)
        return {"error": err}
        
    total_value = 0
    item_count = 0

    try:
        with open(filepath, mode="r") as file:
            reader = csv.DictReader(file)     
            for row in reader:
                quantity = int(row['quantity'])
                unit_cost = float(row['unit_cost'])
                total_value += quantity * unit_cost
                item_count += quantity
    except (ValueError, KeyError) as e:
        err = f"Data corruption or missing column in inventory.csv ({str(e)})"
        log_error("resource_manager", err)
        return {"error": err}
            
    return {
        "total amount used": total_value,
        "total equipments": item_count,
    }
