# FileHashingMD5CLI
# MD5 Hash Calculator CLI

This Python application provides a Command-Line user interface (CLI) for calculating MD5 hash values of files. It allows users to select for a file, calculate its hash, and optionally save the hash to a file or compare it with previously stored hashes.

## Usage
### Prerequisites

- Python 3.x installed

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BRQQQQQ/FileHashingMD5CLI.git
2. Navigate to the project directory:
   ```bash
    cd FileHashingMD5CLI
    ```
3. Run the application:
   ```bash
    python hashCalCLI.py [file_path] [--save] [--compare]
    ```
## Options

- **file_path**: Path to the file for hashing.
- **--save**: Optional flag to save the hash to a file..
- **--compare**: Optional flag to compare the hash with stored hashes.

### Examples

- Calculate the hash of a file:
   ```bash
    python hashCalCLI.py path/to/your/file.tx
    ```
- Calculate the hash and save it to a file:
   ```bash
    python hashCalCLI.py path/to/your/file.tx --save
    ```
- Compare the hash with stored hashes:
   ```bash
    python hashCalCLI.py path/to/your/file.tx --compare
    ```
