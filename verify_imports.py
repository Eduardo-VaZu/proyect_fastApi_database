import sys
import os

# Add the project root to sys.path
sys.path.append(os.getcwd())

try:
    from app.main import app

    print("Import successful!")
except Exception as e:
    print(f"Import failed: {e}")
    sys.exit(1)
