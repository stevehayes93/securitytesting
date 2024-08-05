data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 22},
]

import pickle

def load_serialized_data(filename):
    """
    Load serialized data from a file.

    Args:
        filename (str): Path to the serialized data file.

    Returns:
        object: Deserialized data.
    """
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    serialized_file = 'serial'
    loaded_data = load_serialized_data(serialized_file)
    if loaded_data:
        print("Deserialized data:")
        for item in loaded_data:
            print(item)
