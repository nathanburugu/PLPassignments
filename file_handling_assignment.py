def create_file():
    try:
        # Create a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Hello, this is line 1\n")
            file.write("12345\n")
            file.write("Line 3 with a mix of strings and numbers\n")
        print("File created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
    finally:
        file.close()

def read_and_display_file():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read the contents of the file and display them on the console
            print("Contents of my_file.txt:")
            print(file.read())
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        file.close()

def append_to_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("Additional line 1\n")
            file.write("67890\n")
            file.write("Line 6 appended\n")
        print("File appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        file.close()

# File Creation
create_file()

# File Reading and Display
read_and_display_file()

# File Appending
append_to_file()
