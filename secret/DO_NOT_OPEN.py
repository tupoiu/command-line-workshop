# A python file for a script which takes in the first input and if it's correct (matches the secret) will unzip the zip file and paste the output to treasure_chest.png

import hashlib
import zipfile
import sys

# Define the secret and file paths
SECRET = "aa97302150fce811425cd84537028a5afbe37e3f1362ad45a51d467e17afdc9c"
ZIP_FILE = "hidden_treasure.zip"
OUTPUT_PATH = "treasure_chest"


def main():
    # Get the first command line arg
    if len(sys.argv) < 2:
        print("Usage: python DO_NOT_OPEN.py <secret>")
        sys.exit(1)
    arg = sys.argv[1]
    
    def hash_str(arg):
        # Hash the input using SHA-256
        return hashlib.sha256(arg.encode()).hexdigest()
    print(hash_str(arg))
    print(arg)
    # Check if the input matches the secret
    if hash_str(arg) == SECRET:
        print("Secret is correct! Unzipping the file...")
        try:
            # Unzip the file
            with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
                zip_ref.extractall(OUTPUT_PATH)
            print(f"File extracted successfully to {OUTPUT_PATH}")
        except FileNotFoundError:
            print(f"Error: {ZIP_FILE} not found.")
    else:
        print("Incorrect secret. Access denied.")

if __name__ == "__main__":
    main()

