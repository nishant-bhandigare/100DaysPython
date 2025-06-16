import pandas as pd

df = pd.read_csv(r"day_26\nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter:row.code for (index, row) in df.iterrows()}

# print(nato_dictionary)

user_input = input("Enter the word").strip()

# result = {letter:code for (letter, code) in nato_dictionary.items() if letter in user_input.upper()}
result = {letter:nato_dictionary[letter] for letter in user_input.upper()}
print(result)