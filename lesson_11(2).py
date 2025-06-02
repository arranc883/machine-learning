import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

#we are setting the delimiter as ; as this is what seperates the text from the target variable in the data set , and we are using names= to define the names of the text and the target
test=pd.read_csv(r'C:\Users\arran_te5ei3b\OneDrive\Desktop\machine learning\data_sets\test.txt',delimiter=';',names=['text' , 'target'])
train=pd.read_csv(r'C:\Users\arran_te5ei3b\OneDrive\Desktop\machine learning\data_sets\train.txt',delimiter=';',names=['text' , 'target'])

print(train['target'].unique())
#['sadness' 'anger' 'love' 'surprise' 'fear' 'joy']
#computer doesnt know the difference between love surprise joy ect
#we are making two categories for the computer do decide from : postive emotions and negative emotions

#replacing data with the 2 diffenert options using a dictoinary
#these two things to choose from is stored in the paramenter data
def encoding(data):
    return data.replace({'surprise' : 1 , 'love' : 1 , 'joy' : 1 , 'sadness' : 0 , 'anger' : 0 , 'fear' : 0})

#encoding the train(tagert) to give us the two options for the comupter to decide from
train['target'] = encoding(train['target'])



    
