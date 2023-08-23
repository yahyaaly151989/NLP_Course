import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
import re

# Paragraph containing the text
paragraph = """
Alice's intelligence and dedication have always set her apart. She is not only incredibly smart but also exceptionally hard working. Her ability to grasp complex concepts quickly and apply them in practical situations is truly impressive. Whether it's solving intricate puzzles or collaborating on challenging projects, Alice's sharp mind and diligent approach shine through. She consistently goes the extra mile to achieve her goals, making her a role model for those who value both intelligence and a strong work ethic.
"""

# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',paragraph)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'[^\w]', ' ', text)  # Remove punctuation

text = text.lower()
print(text)


# Preparing the dataset
sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]

# Training the Word2Vec model
model = Word2Vec(sentences, min_count=1)

# Finding Word Vectors
vector = model.wv['intelligence']

# Most similar words
similar = model.wv.most_similar('intelligence')


print("Most Similar Words to 'intelligence':", similar)


