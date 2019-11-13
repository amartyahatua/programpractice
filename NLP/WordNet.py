from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet
sysnet = wn.synsets('Travel')


word_type = sysnet[0].name()
sysnonym = sysnet[0].lemmas()[0].name()
meaning = sysnet[0].definition()
example = sysnet[0].examples()

print(word_type)
print(sysnonym)
print(meaning)
print(example)

## Find all synonyms and antonyms of a word

#synset = wn.synsets('Worse')

syno = list()
anto = list()

for synset in wn.synsets('Worse'):
    for lemma in synset.lemmas():
        syno.append(lemma.name())
        if (lemma.antonyms()):
            anto.append(lemma.antonyms()[0].name())


first_word = wn.synset("Travel.v.01")
second_word = wn.synset("Walk.v.01")


similarity = str(first_word.wup_similarity(second_word))
print(similarity)


dog = wn.synset('dog.n.01')
print(dog.hypernyms())