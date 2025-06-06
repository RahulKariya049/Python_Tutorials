# Task:
# Write a function that appends a log message to "log.txt"
# The message should include the current timestamp using datetime

# Example:
# [2025-05-31 17:00:10] User logged in
import random
from datetime import datetime

log_messages = ["[USER] logged in..", "[Admin] Registered", "[User] Registered", "[Admin] logged in", "Password changed successfully", "Admin changed password"]

def get_current_time():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return timestamp

def log_append(filepath):
    with open(filepath, "a", encoding='utf-8') as f:
        f.write("[" + get_current_time() + "]" + random.choice(log_messages))

for i in range (1,16):
    log_append("File handling/log.txt")