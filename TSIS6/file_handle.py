import os
import string

def list_directories_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nAll Directories and Files:")
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            print(os.path.join(root, directory))
        for file in files:
            print(os.path.join(root, file))


# path = input("Enter the path: ")
# list_directories_files(path)



#2


def check_path_access(path):
    # Check existence
    if not os.path.exists(path):
        print("Path does not exist.")
        return
    
    # Check readability
    if not os.access(path, os.R_OK):
        print("Path is not readable.")
    else:
        print("Path is readable.")

    # Check writability
    if not os.access(path, os.W_OK):
        print("Path is not writable.")
    else:
        print("Path is writable.")

    # Check executability
    if not os.access(path, os.X_OK):
        print("Path is not executable.")
    else:
        print("Path is executable.")


# path = input("Enter the path: ")
# check_path_access(path)







#3
def test_path(path):
    # Check if the path exists
    if os.path.exists(path):
        print("Path exists.")

        # Get filename and directory portion
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("Path does not exist.")


# path = input("Enter the path: ")
# test_path(path)

#4

def count_lines(filename):
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        print(f"Number of lines in {filename}: {line_count}")

# filename = input("Enter the path of the text file: ")
# count_lines(filename)


#5
def write_list_to_file(filename, lst):
        with open(filename, 'w') as file:
            for item in lst:
                file.write(str(item) + '\n')
        print(f"List has been written to {filename} successfully.")
    

# filename = input("Enter the filename to write the list: ")
# list = input("Enter the list elements separated by space: ").split()
# write_list_to_file(filename, list)


#6
def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w'):
            pass
        print(f"File '{filename}' created successfully.")


# generate_files()

#7
def copy_file(source_file, destination_file):
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")



# source_file = input("Enter the source file name: ")
# destination_file = input("Enter the destination file name: ")
# copy_file(source_file, destination_file)



#8
def delete_file(path):

        # Check if the path exists
        if not os.path.exists(path):
            print(f"File '{path}' does not exist.")
            return

        # Check if the file is accessible
        if not os.access(path, os.F_OK):
            print(f"File '{path}' is not accessible.")
            return

        # Delete the file
        os.remove(path)
        print(f"File '{path}' has been successfully deleted.")


# path = input("Enter the path of the file to delete: ")
# delete_file(path)