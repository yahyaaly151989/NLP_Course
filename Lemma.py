

# Tokenization of paragraphs/sentences
import nltk
nltk.download()
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
paragraph = """Language is a thing of beauty. But mastering a new language from scratch is quite a daunting prospect.  If you have ever picked up a language that wasnot your mother tongue, 
you will relate to this! There are so many layers to peel off and syntaxes to consider it is quite a challenge."""
               
# Tokenizing sentences
sentences = nltk.sent_tokenize(paragraph)
print(sentences)

# Tokenizing words
words = nltk.word_tokenize(paragraph)
print("after tokenization",words)

sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

# Stemming
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)  


print("after stem",sentences) 

sentences = nltk.sent_tokenize(paragraph)
lemmatizer = WordNetLemmatizer()

# Lemmatization
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)   

print("after Lem",sentences)    
    




