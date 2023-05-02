import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phon_dict = {row.letter: row.code for(index, row) in data.iterrows()}
print(phon_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
out_list = [phon_dict[letter] for letter in word]
print(out_list)