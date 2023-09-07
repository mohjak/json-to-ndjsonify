import unittest
import os
import json


class TestNdjsonFiles(unittest.TestCase):

    def setUp(self):
        # Fallback to default directory path
        self.directory_path = os.environ.get('NDJSON_DIR', "./out/")

    def validate_ndjson(self, file_path):
        with open(file_path, 'r') as f:
            line_number = 0
            for line in f:
                line_number += 1
                try:
                    json.loads(line.strip())
                except json.JSONDecodeError as e:
                    self.fail(
                        f"Invalid JSON at line {line_number} in file {file_path}. Error: {e}")

    def test_ndjson_validity_in_directory(self):
        for filename in os.listdir(self.directory_path):
            if filename.endswith(".ndjson"):
                self.validate_ndjson(os.path.join(
                    self.directory_path, filename))


if __name__ == '__main__':
    unittest.main()
