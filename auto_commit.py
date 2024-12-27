import os
import subprocess
from datetime import datetime

# Path to this repository folder
repo_path = os.path.dirname(os.path.abspath(__file__))

# File to update
file_path = os.path.join(repo_path, "logfile.txt")

# Update the text file with the current date
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(file_path, "a") as f:
    f.write(f"System started at: {current_date}\n")

# Change directory to the repo
os.chdir(repo_path)

# Git commands
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"System start log: {current_date}"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error during Git operations: {e}")