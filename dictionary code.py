medical_dict={}
with open("dictionary.txt", "r") as file:
    for line in file:
        if ":" in line:
            parts = line.split(":")
            word = parts[0].split()[-1].strip()
            definition = parts[1].strip()
            medical_dict[word] = definition
print("--- File-Based Medical Dictionary ---")
print("(Type 'quit' to stop searching)")
while True:
    search = input("\nEnter a term to look up: ")
    # Check if the user wants to exit
    if search == "quit":
        break
    if search in medical_dict:
        print(search + ": " + medical_dict[search])
    else:
        print("Term not found.")
