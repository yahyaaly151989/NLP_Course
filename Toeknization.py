

# Tokenization of paragraphs/sentences
import nltk
nltk.download()

paragraph = """Language is a thing of beauty. But mastering a new language 
from scratch is quite a daunting prospect.  If you haveve ever picked up a language that wasnot your mother tongue, 
you will relate to this! There are so many layers to peel off and syntaxes to consider it is quite a challenge."""
               
# Tokenizing sentences
sentences = nltk.sent_tokenize(paragraph)
print(sentences)

# Tokenizing words
words = nltk.word_tokenize(paragraph)
print("after tokenization",words)





