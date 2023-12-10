import argparse, hashlib, os #Importing the required libararies

class FileHashing:
   # Initialize the objects for the FileHashing class.
    def __init__(self, file_path, save_to_file=False, compare_hash=False):
        self.file_path = file_path
        self.save_to_file = save_to_file
        self.compare_hash = compare_hash
        
    #A function to Calculate the MD5 hash value of the file.
    def calculate_hash(self, algorithm='md5'):
        hash_object = hashlib.new(algorithm)
        with open(self.file_path, 'rb') as file:
            while chunk := file.read(8192):
                hash_object.update(chunk)
        return hash_object.hexdigest()

    #A Function to Save the hash value to the "hashes.txt" file.
    def save_hash_to_file(self, hash_value, output_file='hashes.txt'):
        with open(output_file, 'a') as file:
            file.write(f"{self.file_path}: {hash_value}\n")

    #A Function to Compare the hash value of the file with a stored hash.
    def compare_hashes(self, stored_hash, algorithm='md5'):
        current_hash = self.calculate_hash(algorithm)
        return current_hash == stored_hash
    
    #A Function to check the hash
    def execute_hashing(self):
        # Check if the file exists
        if not os.path.exists(self.file_path):
            print("Error: The specified file does not exist.")
            return

        # Calculate & Display the MD5 hash value
        hash_value = self.calculate_hash() # Variable to Store the hash Value calculated from calculate_hash() Function
        print(f"MD5 Hash Value: {hash_value}")

        # Run the save_hash function if the --save option is used
        if self.save_to_file:
            self.save_hash(hash_value)

        # Run the compare_hashes_and_display function if the --compare option is used
        if self.compare_hash:
            self.compare_hashes_and_display(hash_value)

    # Save the hash value to file
    def save_hash(self, hash_value):
        output_file = 'hashes.txt'

        if not os.path.exists(output_file):
            with open(output_file, 'w'):
                pass

        with open(output_file, 'r') as file:
            existing_hashes = file.read()

        if f"{self.file_path}: {hash_value}" not in existing_hashes:
            self.save_hash_to_file(hash_value)
            print("Hash saved successfully.")
        else:
            print("Duplicate hash. This hash already exists in the file.")

    # Compare hashes and display the result
    def compare_hashes_and_display(self, hash_value):
        output_file = 'hashes.txt'

        with open(output_file, 'r') as file:
            existing_hashes = file.readlines()

        for line in existing_hashes:
            parts = line.strip().split(': ', 1)
            if len(parts) == 2:
                stored_file, stored_hash = parts
                if stored_file == self.file_path:
                    if hash_value == stored_hash:
                        print("Hashes match. The file has not been modified.")
                    else:
                        print("Hashes didn't match. The file may have been modified.")
                    break


def main():
    
    parser = argparse.ArgumentParser(description="MD5 Hash Calculator CLI") #Creating an Argument_Parser for the CLI

    # Defining the command-line arguments
    parser.add_argument("file_path", help="Provide the Path to the file for which you want to calculate the hash")
    parser.add_argument("--save", action="store_true", help="Save the hash to a file")
    parser.add_argument("--compare", action="store_true", help="Compare the hash with stored hashes")
    
    args = parser.parse_args() # Parsing the command-line arguments

    # Creating an instance or calling the FileHashing with chosen options
    file_hashing_cli = FileHashing(args.file_path, save_to_file=args.save, compare_hash=args.compare)

    # From the Instance call the execute_hashing function
    file_hashing_cli.execute_hashing()

if __name__ == "__main__":
    main()
