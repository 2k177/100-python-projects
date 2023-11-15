#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    invited_names = file.read()

invited_names = invited_names.split("\n")

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in invited_names:
    file_name = f"letter_for_{name}"
    formatted_string = letter.replace(PLACE_HOLDER, name)
    with open(f"./Output/ReadyToSend/{file_name}", "w") as file:
        file.write(formatted_string)



