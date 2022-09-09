import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(new_dict)
user_name = input("what is your name? : ").upper()
name_list = [new_dict[letter] for letter in user_name]
print(name_list)