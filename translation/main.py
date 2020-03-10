# import nltk
import variables
import parsing
from translation import reorder
import grammar_metadata
import gender_identification
import vibhakti_identification
import translate
import inflection
import pp_removal

# import sandhi

parsing.parse()
# print(variables.s1)
# print(variables.root)
parsing.traverse_tree(variables.root)
print(variables.english)
print("Parse tree:", variables.s1)
reorder.token(variables.root)
print(variables.z)
grammar_metadata.remove_DT()
print("English list:", variables.english)
print("Rearranged tokens:", variables.rearrange)
grammar_metadata.tense_identification()
print(variables.tense)
print("tense is:", variables.tense1)
grammar_metadata.pos_list()
print(variables.rearrange)
print("Rearranged POS:", variables.pos)
grammar_metadata.multi_list()
print("Multiplicity:", variables.multi)
grammar_metadata.degree_list()
print("degree:", variables.degree)
gender_identification.gender_list()
print("gender:", variables.gender)
vibhakti_identification.case_list()
print("case is:", variables.case)
print("dependency is", variables.dependency)
print('translation is')
translate.marathi_list()
print("Lexicons are:", variables.lexicon)
print("Trans. marathi words:", variables.marathi)
inflection.inflection_all()
print('inflection is')
print(variables.marathi)
pp_removal.output()
print("marathi output:", variables.output)
