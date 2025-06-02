#nlp = natural language processing
#understanding emotion behind the text
#aka centimental analysis

#tokenization
#breaking text into individual words 
#nltk = natural language processing

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
#choosing to isntall word tokenizer
from nltk.tokenize import word_tokenize

#text we are tokenizing
text="Natural Language Processing is a subfield of artificial intelligence that focuses on the interaction between humans and computers using natural language."
#e.g 'natural' , 'language' , 'processing

#tokens  =  each word that has been tokenized
tokens=word_tokenize(text)

#printing all the words(that have been tokenized) in a list
#print(tokens)

#stop words from nltk i.e a that and is (conective words that have no meaning)
from nltk.corpus import stopwords

#stop words are stored in variable sw (in a set data struchers which doesnt allow duplicates)
sw=set(stopwords.words('english'))

#showing sw
#print(sw)

#for every tokeniuzed word lower it and check if it is not in sw. if it is remove it
filtered_words = [i for i in tokens if i.lower() not in sw]
print(filtered_words)

#lemmatization
#turns words that are similar into its base word.
#i.e running is turned into run

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

#for every word in filtered word lemmatize it(lemmatizeing i)
filtered_2 = [lemmatizer.lemmatize(i) for i in filtered_words]

#checking if it works
print(filtered_2)
