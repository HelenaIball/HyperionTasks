#----------copy from task file #1----------
import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#the results of this were interesting as they showed a closer similarity between the two animals than an animal and the fruit
#Spacy also identified a relationship between bananas and monkeys
#this was specific to monkeys eating bananas as there was not an equal similarity between the cat and the fruit
#I have come up with my own example below

word4 = nlp('house')
word5 = nlp('bungalow')
word6 = nlp('stairs')

print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

#this shows a close similarity between house and bungalow as these are both places one lives
#it shows a stronger similarity between a house and stairs compared to a bungalow and stairs

#----------copy from task file #2----------
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


#----------copy from task file #3----------
sentence_to_compare = 'Why is my cat on the car'

sentences = ['where did my dog go',
'Hello, there is my car',
"I've lost my car in my car",
"I'd like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-", similarity)

#when running the example file with the simplier en_core_web_sm model I received the following message:
#'The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements.'
#The output showed very different results with most sentences appearing less similar than when the en_core_web_md model was used.