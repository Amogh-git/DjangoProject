from translation import variables
import random
from nltk.corpus import names
from nltk.corpus import words


def gender_features(word):  # to train naive bayes classifier
    return {'last_letter': word[-1]}


words.fileids()
words.words('en')
names.fileids()
g1 = names.words('C:\\Projects\\Project_M\\translation\\Reference_Files\\male.txt')
g2 = names.words('male.txt')
i = 0
while i < len(g1):
    g2.append(g1[i])
    i = i + 1
g3 = names.words('C:\\Projects\\Project_M\\translation\\Reference_Files\\female.txt')
g4 = names.words('C:\\Projects\\Project_M\\translation\\Reference_Files\\female.txt')
i = 0
while i < len(g3):
    g4.append(g3[i])
    i = i + 1
g5 = 'C:\\Projects\\Project_M\\translation\\Reference_Files\\neuter.txt'
g6 = names.words(g5)

male_names = [(name, 'male') for name in names.words('male.txt')]
female_names = [(name, 'female') for name in names.words('female.txt')]
neuter_names = [(name, 'neuter') for name in names.words(g5)]
labeled_names = male_names + female_names + neuter_names

random.shuffle(labeled_names)
from nltk import NaiveBayesClassifier

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = NaiveBayesClassifier.train(train_set)


def gender_list():
    i = 0
    while i < len(variables.rearrange):  # to identify gender of tokens
        if variables.pos[i] == "PRP" or variables.pos[i] == "PRP$":
            if (variables.rearrange[i].lower() == "i" or variables.rearrange[i].lower() == "you" or variables.rearrange[
                i].lower() == "they" or variables.rearrange[i].lower() == "we"):
                variables.gender.append('b')
            elif variables.rearrange[i].lower() == "he":
                variables.gender.append('m')
            elif variables.rearrange[i].lower() == "she":
                variables.gender.append('f')
            elif variables.rearrange[i].lower() == "it":
                variables.gender.append('n')

        elif (variables.pos[i] == "NN" or variables.pos[i] == "NNP" or variables.pos[i] == "NNPS" or variables.pos[
            i] == "NNS"):
            g = classifier.classify(gender_features(variables.rearrange[i]))
            if g == 'male':
                variables.gender.append('m')
            elif g == 'female':
                variables.gender.append('f')
            else:
                variables.gender.append('n')

        else:
            variables.gender.append(-1)
        i = i + 1


#print(variables.gender)
