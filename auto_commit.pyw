import os
import subprocess
from datetime import datetime

# Path to the repository folder
repo_path = r"C:\activity_log"

# File to update with the timestamp
file_path = os.path.join(repo_path, "logfile.txt")

# Update the text file with the current date
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(file_path, "a") as f:
    f.write(f"System started at: {current_date}\n")

# Change to the repository directory
os.chdir(repo_path)

# Run Git commands
subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(["git", "commit", "-m", f"System start log: {current_date}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(["git", "push", "origin", "main"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
