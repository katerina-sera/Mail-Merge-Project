#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as name_list:
    new_list = name_list.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    f = letter.read()
    for index in range(len(new_list)):
        word = new_list[index]
        new_name = word.strip()
        new_text = f.replace("[Name]", new_name)
        with open("./Output/ReadyToSend/sending_letters_"+str(index+1)+".txt", "w+") as new_letter:
            new_letter.write(new_text)

