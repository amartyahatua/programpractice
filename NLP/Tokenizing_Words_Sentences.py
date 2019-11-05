from nltk.tokenize import sent_tokenize, word_tokenize

## Word and Sentence tokenizer ##

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."

print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)

## Stop words ##
## Some word which we dont care about ##

from nltk.corpus import  stopwords
example_sentence = "This is an example of stop word showing off"
stop_words = set(stopwords.words("english"))
words = word_tokenize(example_sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence)
filtered_sentence.clear()

filtered_sentence = [w for w in words if w not in stop_words]
print(filtered_sentence)


## Stemming ##

# I was taking a ride in the car
# I was riding in the car

from  nltk.stem import PorterStemmer

ps = PorterStemmer()
example_words = ['python', 'pythoner', 'pythoning', 'pythoned', 'pythonly']
for w in example_words:
    print(ps.stem(w))
