import nltk
from translation import variables

from stanfordcorenlp import StanfordCoreNLP
import string

c = ''


def parse():
    sentence = 'Planetary science is the study of the assemblage of planets, moons, dwarf planets, comets, asteroids, and other bodies orbiting the Sun, as well as extrasolar planets. While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
    nlp = StanfordCoreNLP(r'C:\Projects\stanford-corenlp-full-2018-02-27')
    for c in string.punctuation:  # to remove punctuation
        variables.sentence = variables.sentence.replace(c, "")

    variables.s1 = nlp.parse(variables.sentence)  # to parse sentence
    variables.s1 = variables.s1.lstrip('(ROOT')  # to remove root node from parsed output

    variables.s1 = variables.s1[:-1]
    print('Constituency Parsing:', variables.s1)

    nlp.close()

    variables.root = nltk.tree.Tree.fromstring(variables.s1)  # to convert parse tree to string
    print(variables.root)


flag = 0


def traverse_tree(tree):  # to print words and its pos
    #print("tree:", tree)
    #    global english
    global flag
    for subtree in tree:
        if type(subtree) == nltk.tree.Tree:
            traverse_tree(subtree)
            if flag == 1:
                variables.english.append(nltk.tree.Tree.label(subtree))
                flag = 0
        elif nltk.tree.Tree.leaves(subtree):
            variables.english.append(subtree)
            flag = 1


#parse()
#traverse_tree(variables.root)
