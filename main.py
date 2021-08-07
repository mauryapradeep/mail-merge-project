PLACEHOLDER = "[name]"
with open("./input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()


with open("./input/Letters/starting_letter.txt") as starting_letter :
    letter_contents = starting_letter.read()

    for name in names:
        striped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, striped_name)


    with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)






