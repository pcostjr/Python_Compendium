# read_write.py
# description: A simple program that demonstrates file read & write in Python
# author: pcostjr
# created: 1.6.2026
# last update: 1.6.2026

# i'm using os specifically to check for any filepath, but we're mainly working with local filepaths
# it is not imperative that you include it
import os


# read the contents of a file (if it exists).
def read_file():
    # in this context we need to include the file extension (ex: 'hello.txt)
    filename = input("[-] Please enter the full filename to read: ")

    try:
        # attempt to read the contents of the file
        with open(filename, 'r') as file:
            contents = file.read()
            print(f"[-] Contents of '{filename}'\n:")
            # contents is stored as a string, so we can just throw it to print
            print("   " + contents + "\n")

    except FileNotFoundError:
        # we account for FNF since it's the most likely issue
        print(f"\n[!] Error: File '{filename}' not found.\n"
              f"\n[?] Did you make sure to enter the filename correctly?\n")
        # general error case in the event the file is corrupted or gets deleted mid-read
    except Exception as e:
        print(f"[!] Error reading file '{filename}': {e}\n")


# write to an existing or new file.
def write_file():
    message = input("[-] Enter the message to write: ")
    filename = input("[-] Enter the filename to write to: ")

    # check if file exists
    # os.path will read any filepath, but since we're storing and working with these locally
    # the local path is simply the filename
    if os.path.exists(filename):
        print(f"\n[!] Warning: File '{filename}' already exists.")
        choice = input("\n[?] Do you want to (O)verwrite or write to a (N)ew file? ").upper()

        if choice == 'N':
            # have user submit new filename
            filename = input("\n[-] Enter new filename: ")
        elif choice != 'O':
            # otherwise, check if they want to overwrite, escape if neither
            print("[!] Invalid choice. Operation cancelled.\n")
            return
    try:
        # we push a string to the file to write to it
        # at this point, we do not care what the filename is and assume
        # we can write to it without issue
        # if the file does not exist, a new one with the filename will be made
        # if it does, the file will be completely overwritten
        with open(filename, 'w') as file:
            file.write(message)
        print(f"\n[✓] Message successfully written to '{filename}'.\n")

    except Exception as e:
        # if there is any issue, error out
        print(f"\n[!] Error writing to file: {e}\n")


# main method declaration
def main():
    while True:
        print("[-] Welcome to ReadWrite!\n"
              "[-] 0. Exit\n"
              "[-] 1. Read File\n"
              "[-] 2. Write File\n")
        choice = input("[-] Enter your choice (0-3): ")

        if choice == '0':
            # exit the program
            print("\n[✓] Exiting.\n")
            exit()
        elif choice == '1':
            # call the read file method
            read_file()
        elif choice == '2':
            # call the write file method
            write_file()
        else:
            print("\n[!] Invalid choice. Please enter a value from 0-2.")


if __name__ == "__main__":
    main()
