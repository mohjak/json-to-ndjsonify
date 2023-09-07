import json
import os
import sys
from datetime import datetime
import argparse


def find_first_key_in_dict(d, target_key):
    if target_key in d:
        return d[target_key]

    for key, value in d.items():
        if isinstance(value, dict):
            result = find_first_key_in_dict(value, target_key)
            if result is not None:
                return result
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    result = find_first_key_in_dict(item, target_key)
                    if result is not None:
                        return result
    return None


def extract_first_target_node_from_json(json_file_path, target_key, output_folder_path):

    # Generate timestamp suffix
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    # Generate output file name with timestamp suffix
    output_file_name = f"{os.path.splitext(os.path.basename(json_file_path))[0]}_{timestamp}.ndjson"

    # Use the provided output folder for the output file, default to input folder if not provided
    if output_folder_path is None:
        output_folder_path = os.path.dirname(json_file_path)

    output_ndjson_file_path = os.path.join(
        output_folder_path, output_file_name)

    # Read the JSON data from the file
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Search for the first occurrence of the target key
    first_target = find_first_key_in_dict(json_data, target_key)

    # If the target key is found, write to the .ndjson file
    if first_target is not None:
        with open(output_ndjson_file_path, 'w') as ndjson_file:
            for edge in first_target:
                ndjson_file.write(json.dumps(edge) + '\n')
    else:
        print(f"The key '{target_key}' could not be found in the JSON data.")


def entry_point():
    parser = argparse.ArgumentParser(description='Convert JSON to NDJSON.')
    parser.add_argument('--input', type=str,
                        help='Path to the input JSON file.')
    parser.add_argument('--node', type=str,
                        help='Name of the node to extract.')
    parser.add_argument('--output', type=str,
                        help='Path to the output folder.')

    args = parser.parse_args()

    if args.input is None or args.node is None:
        print("--input, --node, and --output parameters must be provided.")
        sys.exit(1)

    extract_first_target_node_from_json(args.input, args.node, args.output)


if __name__ == '__main__':
    entry_point()
