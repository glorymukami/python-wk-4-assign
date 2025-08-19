# File Read & Write with Error Handling + Example Content 🖋️🧪

def process_file():
    filename = input("Enter the filename to read (e.g., input.txt): ")

    try:
        # Step 1: Try reading the input file
        with open(filename, "r") as infile:
            content = infile.read()
            print("\n📖 Original content:")
            print(content)

    except FileNotFoundError:
        # If file doesn't exist, create it with example content
        example_text = """Hello there!
This is my first file read & write test.
Python is fun.
"""

        with open(filename, "w") as infile:
            infile.write(example_text)

        print(f"\n⚠️ File '{filename}' not found. A new file has been created with example content.")
        
        # Read the new file
        with open(filename, "r") as infile:
            content = infile.read()
            print("\n📖 Original content:")
            print(content)

    except PermissionError:
        print(f"🚫 Error: You don't have permission to read '{filename}'.")
        return
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
        return

    # Step 2: Modify content (convert to uppercase)
    modified_content = content.upper()

    # Step 3: Write to new file
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("\n✅ Modified content has been written to 'output.txt'")


# Run the program
process_file()
