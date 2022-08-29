def reverse_each_word(sentence):
    return " ".join([x[::-1] for x in sentence.split()])

print(reverse_each_word("Subscribe to BHUVI CODES"))
