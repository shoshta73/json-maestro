import json
import os
import sys
import re
from typing import Union, List, Dict, Any, cast, TypeVar, Set, TYPE_CHECKING

T = TypeVar('T')

if TYPE_CHECKING:
    from typing_extensions import Literal

def load_jsonc(file_path: str) -> Dict[str, Any]:
    """Load JSONC from a file, skipping comments starting with // and handling control characters."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Remove comments starting with //
            content = re.sub(r'//.*\n', '', content)

            # Handle control characters
            content = re.sub(r'[^\x20-\x7E]', '', content)

            # Parse the remaining content as JSON
            return json.loads(content)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in the file. Error details: {str(e)}")
        print("Please check the contents of the file.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Unexpected content in the file. Error details: {str(e)}")
        print("Please check the contents of the file.")
        sys.exit(1)
    return json.loads(content)

def load_vscode_settings(file_path: str) -> Dict[str, Any]:
    """Load VSCode settings.json file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Remove comments starting with //
            content = re.sub(r'//.*\n', '', content)
            # Parse the remaining content as JSON
            return json.loads(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in the file. Error details: {str(e)}")
        print("Please check the contents of the file.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Unexpected content in the file. Error details: {str(e)}")
        print("Please check the contents of the file.")
        sys.exit(1)


def remove_comments(obj: Union[Dict[str, Any], List[Any], Any]) -> Union[Dict[str, Any], List[Any], Any]:
    """Remove comments from the object."""
    if isinstance(obj, dict):
        return {k: remove_comments(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [remove_comments(item) for item in obj]
    else:
        return obj

def remove_duplicate_keys(obj: Union[Dict[str, Any], List[Any], Any]) -> Union[Dict[str, Any], List[Any]]:
    """
    Recursively remove duplicate keys from a nested object.

    Args:
    obj: A dictionary, list, or any other object to process.

    Returns:
    A dictionary, list, or any other object with duplicate keys removed.
    """
    def _remove_duplicates_helper(obj: Union[Dict[str, Any], List[Any]]) -> Union[Dict[str, Any], List[Any]]:
        if isinstance(obj, dict):
            new_obj: Dict[str, Any] = {}  # Explicitly declare the type
            seen_keys: Set[str] = set()  # Explicitly declare the type
            for key, value in obj.items():
                if key not in seen_keys:
                    seen_keys.add(key)
                    new_obj[key] = _remove_duplicates_helper(value)
            return new_obj
        elif isinstance(obj, list):
            return [_remove_duplicates_helper(item) for item in obj]
        else:
            return obj

    return _remove_duplicates_helper(obj)

def add_schema_keys(obj: T) -> T:
    """
    Add schema-related keys to the object.

    Args:
    obj: An object (dictionary, list, or any other type) to process.

    Returns:
    The processed object with schema-related keys added.
    """
    if isinstance(obj, dict):
        if "json.schemas" not in obj:
            obj["json.schemas"] = []
        for key, value in obj.items():
            if isinstance(value, list) and key.startswith("json.schemas"):
                for item in value:
                    if "fileMatch" not in item:
                        item["fileMatch"] = []
                    if "url" not in item:
                        item["url"] = ""
    elif isinstance(obj, list):
        for item in obj:
            add_schema_keys(item)
    return obj

def sort_json_keys(obj: T, reverse: bool = False) -> T:
    """
    Sort dictionary keys recursively.

    Args:
    obj: An object (dictionary, list, or any other type) to process.
    reverse: Whether to sort in descending order (default is ascending).

    Returns:
    The processed object with sorted keys.
    """
    def _sort_dict_items(items: Dict[str, T]) -> Dict[str, T]:
        return dict(sorted(items.items(), key=lambda x: x[0], reverse=reverse))

    if isinstance(obj, dict):
        if not obj:
            return obj  # Handle empty dictionaries

        return {k: sort_json_keys(v, reverse) for k, v in _sort_dict_items(obj)}
    elif isinstance(obj, list):
        return [sort_json_keys(item, reverse) for item in obj]
    else:
        return obj

def save_json(data: Union[dict, list, str, int, float, bool], file_path: str):
    """
    Save JSON data to a file.

    Args:
    data: The JSON data to be saved. Can be a dictionary, list, string, integer, float, or boolean.
    file_path: The path to the file where the JSON data will be saved.

    Raises:
    ValueError: If the input data is not a valid JSON serializable object.
    IOError: If there's an issue writing to the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
    except IOError as e:
        print(f"Error: Unable to write to file '{file_path}'. Error: {str(e)}")
        sys.exit(1)
    except TypeError as e:
        raise ValueError(f"Invalid JSON data: {str(e)}")

def main():
    input_file = input("Enter the path to your JSON, JSONC, or VSCode settings.json file: ")

    # Check if it's a VSCode settings.json file
    if input_file.endswith('.json'):
        load_function = load_vscode_settings
    else:
        load_function = load_jsonc

    # Load the input file
    try:
        original_data = load_function(input_file)
    except Exception as e:
        print(f"Failed to load input file. Error: {str(e)}")
        sys.exit(1)

    # Process the data
    try:
        cleaned_data = remove_duplicate_keys(original_data)
        cleaned_data = add_schema_keys(cleaned_data)

        # Remove comments if requested
        remove_comments_option = input("Do you want to remove comments? (y/n): ").lower()
        if remove_comments_option == 'y':
            cleaned_data = remove_comments(cleaned_data)

        # Sort the keys
        sort_order = input("Do you want to sort keys? (y/n): ").lower()
        if sort_order == 'y':
            sort_method = input("Do you want to sort in ascending (a) or descending (d)? ").lower()
            if sort_method == 'a':
                cleaned_data = sort_json_keys(cleaned_data, reverse=False)
            elif sort_method == 'd':
                cleaned_data = sort_json_keys(cleaned_data, reverse=True)
            else:
                print("Invalid choice. Defaulting to ascending order.")
                cleaned_data = sort_json_keys(cleaned_data, reverse=False)
    except Exception as e:
        print(f"Failed to process data. Error: {str(e)}")
        sys.exit(1)

    # Save the cleaned data to the output file
    output_file = f"{os.path.splitext(input_file)[0]}_clean{os.path.splitext(input_file)[1]}"
    try:
        save_json(cleaned_data, output_file)
    except Exception as e:
        print(f"Failed to save cleaned data. Error: {str(e)}")
        sys.exit(1)

    print(f"Successfully processed {input_file}")
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    main()