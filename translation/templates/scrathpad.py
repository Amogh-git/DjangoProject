from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize


"""import spacy      # NER using spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

nlp = en_core_web_sm.load()
#text = "Cane fruits such as the black raspberry and the boysenberry root easily and
# economically by tip layering, one form of natural layering."

doc = nlp('Cane fruits such as the black raspberry and the boysenberry root easily and economically by tip layering, one form of natural layering.')

a = []
print([(X.text, X.label_)
       for X in doc.ents])"""
st = StanfordNERTagger('C:/Projects/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz',
                       'C:/Projects/stanford-ner-2017-06-09/stanford-ner.jar', encoding='utf-8')
text = "Cane fruits such as the black raspberry and the boysenberry root easily and economically by tip layering, one form of natural layering."
tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)
for i in classified_text:
    print(i)
