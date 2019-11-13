from nltk.corpus import wordnet as wn

sysnet = wn.synsets('Travel')


word_type = sysnet[0].name()
sysnonym = sysnet[0].lemmas()[0].name()
meaning = sysnet[0].definition()
example = sysnet[0].examples()

print(word_type)
print(sysnonym)
print(meaning)
print(example)