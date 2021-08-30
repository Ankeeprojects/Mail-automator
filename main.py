#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open("Input/Names/invited_names.txt") as invites:
    nomes = invites.readlines()

with open("Input/Letters/starting_letter.txt") as t:
    template = t.read()

for nome in nomes:
    nome = nome.strip()
    path = "Output/ReadyToSend/letter_to_" + nome + ".txt"
    with open(path, 'w') as escrita:
        escrita.write(template.replace("[name]", nome))
