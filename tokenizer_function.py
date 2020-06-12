import string
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English

def spacy_tokenizer(text):
    
    # Create our list of punctuation marks
    punctuations = string.punctuation

    # Create our list of stopwords
    nlp = spacy.load('en_core_web_sm')
    stop_words = spacy.lang.en.stop_words.STOP_WORDS

    # Adding words to remove in addition to stopwords
    add_stopwords = ['machine', 'learning'] # All patents in dataset contain these terms
    
    # remove numbers and special characters
    pattern = '[0-9]'
    cleantext = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    cleantext2 = re.sub(pattern, '', cleantext)
    
    # remove html tags
    html = re.compile('<.*?>')
    cleantext3 = re.sub(html, '', cleantext2)
    
    # Creating token object
    doc = nlp(cleantext3)

    entity_list = []
    for token in list(doc.ents):
        entities = str(token).split(' ')
        for word in entities:
            entity_list.append(word)
    tokens = [word for word in doc if word.text not in entity_list]

    # Lemmatizing each token and converting each token into lowercase
    tokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in tokens ]

    # Removing stop words
    tokens = [ word for word in tokens if word not in stop_words and word not in punctuations ]
    
    # Removing custom set of terms
    tokens = [ word for word in tokens if word not in add_stopwords ]

    # remove words with less than 3 characters
    tokens = [ word for word in tokens if len(word) > 2 ]

    # return preprocessed list of tokens
    return tokens