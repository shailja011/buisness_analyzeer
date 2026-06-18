import os
from datetime import datetime

def log_error(module_name, error_message):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_filepath = os.path.join(log_dir, "error.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_filepath, mode = "a") as file:
        file.write(f"[{timestamp}] [MODULE: {module_name.upper()}] ERROR: {error_message}\n")