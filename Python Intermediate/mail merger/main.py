#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp4

with open(r"Intermediate\mail merger\Mail Merge Project Start\Input\Names\invited_names.txt") as name_file:
    name_list = name_file.readlines()

for i in range(0, len(name_list)):
    stripped_name = name_list[i].strip()
    
    with open(r"Intermediate\mail merger\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter:
        invitation_text =  letter.read()
        with open(r"Intermediate\mail merger\Mail Merge Project Start\Output\ReadyToSend\letter_for_"+stripped_name+".txt", "w") as new_invitation:
            invitation_text = invitation_text.replace("[name]", f"{stripped_name}")
            new_invitation.write(invitation_text) 