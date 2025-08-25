import os
import sys
import subprocess
import sqlite3
from pathlib import Path

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

print("🚀 TorScope Pro v6.0 - Setup & Launch")

# Create folders
for f in ['data', 'screenshots', 'logs', 'plugins']:
    Path(f).mkdir(exist_ok=True)
    print(f"✅ {f}/")

# Install deps
run(f"{sys.executable} -m pip install -r requirements.txt")

# Init DB
db = Path('data/torscope_data.db')
if not db.exists():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS search_results (id INTEGER PRIMARY KEY, timestamp TEXT, query TEXT, url TEXT, verification_status TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS uptime_log (url TEXT, timestamp TEXT, status TEXT)''')
    conn.commit()
    conn.close()
    print("✅ Database created")

# Launch app
print("🎮 Launching TorScope Pro...")
run(f"{sys.executable} main.py")