# open the starting letter file
with open('../Mail Merging/Input/Letters/starting_letter.txt', 'r') as starting_letter:
    # read content as a string from starting letter to be modified latter
    letter_content = starting_letter.read()
    #open the invited names file
    with open('./Input/Names/invited_names.txt', 'r') as invited_names:
        # reads each line of content into a list to iterate through each name
        names = invited_names.readlines()
        # for each name in invited_names.txt
        for name in names:
            invitee = name.strip()  # removes spaces from each name for formatting
            # creates new file per invitee by opening (Save the letters in the folder "ReadyToSend".)
            with open(f'../Mail Merging/Output/ReadyToSend/letter_to_{invitee}', 'w') as new_letter:
                # Replace the [name] placeholder with the actual name.
                new_letter_content = letter_content.replace('[name]', invitee)
                new_letter.write(new_letter_content)  # writes new content in each letter


# useful hints for file writting and transformation.
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
