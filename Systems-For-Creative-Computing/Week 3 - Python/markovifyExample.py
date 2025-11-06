#!/usr/bin/env python3

import markovify

# Get raw text as string.
with open("Frankenstein.txt") as file:
    text1 = file.read()
    
with open("Emma.txt") as file:
	text2 = file.read()

# Build the model.
text_model1 = markovify.Text(text1)
text_model2 = markovify.Text(text2)

model_combo = markovify.combine([text_model1, text_model2])

# Print five randomly-generated sentences
for i in range(5):
    print(model_combo.make_sentence())
    print()

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(model_combo.make_short_sentence(150))
    print()
