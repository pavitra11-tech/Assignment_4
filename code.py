#Task 1: Read a File and Handle Errors 

try:
    with open("sample.txt", 'r') as fh:
        print("Reading the contents of the file")
        for line_number, line in enumerate(fh, start=1):
            print(f'Line{line_number}: {line.strip()}')
except FileNotFoundError:
    print("The file sample.txt was not found")



#Task 2: Write and Append Data to a File

data = input("Enter text to write: ")

with open("output.txt","wt") as fh:
    fh.write(data + "\n")
    print("Data successfully written to output.txt")

additional_data = input("Enter additional text to append: ")

with open("output.txt", 'at') as fh:
    fh.write(additional_data + "\n")
    print("Data successfully appended.")

with open("output.txt", "r") as fh:
    print("Final content of output.txt:")
    print(fh.read())
