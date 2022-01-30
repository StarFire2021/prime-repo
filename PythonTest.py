import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        print("No previous file exists. Creating default dictionary.")
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)

    if command == "save":
        key = input("Enter your key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print("Data Saved Successfully.")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    elif command == "delete":
        key = input("Enter a key to delete: ")
        data.pop('Testing')
        save_items(SAVED_DATA, data)
        print(key)       
    elif command == "clear":
        data.clear()
        save_items(SAVED_DATA, data)
        print('All items cleared.')       
    else:
        print("Unknown Command")
else:
    print("Please pass exactly one command.")