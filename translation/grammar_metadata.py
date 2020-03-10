from translation import variables
from nltk import word_tokenize

def remove_DT():
    variables.rearrange=word_tokenize(variables.z)
    i=0
    while i<len(variables.english):  #to remove pos named DT from parsed array
        if \
        variables.english[i].lower()== 'a' or variables.english[i].lower()== 'an' or variables.english[i].lower()== 'the':
            variables.english.remove(variables.english[i])
            variables.english.remove(variables.english[i])
        i=i+2

#print(variables.english)

    i=0
    while i<len(variables.rearrange): # to remove a, an, the from rearranged array
        if \
        variables.rearrange[i].lower()== 'a' or variables.rearrange[i].lower()== 'an' or variables.rearrange[i].lower()== 'the':
            variables.rearrange.remove(variables.rearrange[i])
            continue
        else:
            i=i+1

#print(variables.rearrange)

def tense_identification():
    i=1
    while i<len(variables.english): # to identify tense of sentence
        if variables.english[i]== "MD":
            variables.tense="future"
            if variables.english[i + 1].lower()== "be":
               variables.tense1="continuous future "
            elif variables.english[i + 1].lower()== "have":
                if variables.english[i + 3].lower()== "been":
                    variables.tense1="perfect continuous future"
                else:
                    variables.tense1=" perfect future"
            else:
                    variables.tense1="simple future"
            break
        elif variables.english[i]== "VBN" or  variables.english[i]== "VBD":
            variables.tense="past"
            if variables.english[i - 1].lower()== "was" or  variables.english[i - 1].lower()== "were":
               variables.tense1="continuous past "
            elif variables.english[i - 1].lower()== "had":
                if variables.english[i + 1].lower()== "been":
                    variables.tense1="perfect continuous past"
                else:
                    variables.tense1=" perfect past"
            else:
                    variables.tense1="simple past"
            break
        elif variables.english[i]== "VB" or  variables.english[i]== "VBG" or  variables.english[i]== "VBP" or  variables.english[i]== "VBZ":
            variables.tense="present"
            if variables.english[i - 1].lower()== "am" or  variables.english[i - 1].lower()== "is" or  variables.english[i - 1].lower()== "are":
               variables.tense1="continuous present "
            elif variables.english[i - 1].lower()== "have" or  variables.english[i - 1].lower()== "has":
                if variables.english[i + 1].lower()== "been":
                    variables.tense1="perfect continuous present"
                else:
                    variables.tense1=" perfect present"
            else:
                    variables.tense1="simple present"
            break
        else:
            i=i+2



'''
def tense_identification():
    i=1
    while i<len(variables.english): # to identify tense of sentence
        if (variables.english[i]=="MD"):
            variables.tense="future"  
            break
        elif (variables.english[i]=="VBN" or  variables.english[i]=="VBD"):
            variables.tense="past" 
            break
        elif (variables.english[i]=="VB" or  variables.english[i]=="VBG" or  variables.english[i]=="VBP" or  variables.english[i]=="VBZ"):
            variables.tense="present"
            break
        else:
            i=i+2
         
#print(variables.tense)
'''
def pos_list():
    i=0
    while i<len(variables.rearrange):  # to create seperate array of POS
        j=0
        while j<len(variables.english):
            if variables.english[j].lower()==variables.rearrange[i].lower():
                variables.pos.append(variables.english[j+1])
                break
            else:
                j=j+2
        i=i+1

# print(variables.rearrange)
# print(variables.pos)

def multi_list():
    i=0
    while i<len(variables.rearrange):  # to identify multiplicity of tokens
        if variables.pos[i]== "NN" or variables.pos[i]== "NNP" or variables.pos[i]== "VBD" or variables.pos[i]== "VB" or variables.pos[i]== "VBZ":
            variables.multi.append("s")
        elif variables.pos[i]== "NNS" or variables.pos[i]== "NNP":
            variables.multi.append("p")
        elif variables.pos[i]== "PRP" or variables.pos[i]== "PRP$":
            if variables.rearrange[i].lower()== "I".lower() or variables.rearrange[i].lower()== "Me".lower() or variables.rearrange[i].lower()== "My".lower() or variables.rearrange[i].lower()== "Mine".lower() or variables.rearrange[i].lower()== "He".lower() or variables.rearrange[i].lower()== "She".lower() or variables.rearrange[i].lower()== "It".lower() or variables.rearrange[i].lower()== "His".lower() or variables.rearrange[i].lower()== "Him".lower() or variables.rearrange[i].lower()== "Her".lower() or variables.rearrange[i].lower()== "You".lower() or variables.rearrange[i].lower()== "Your".lower() or variables.rearrange[i].lower()== "Yours".lower():
                variables.multi.append("s")
            elif variables.rearrange[i].lower()== "They".lower() or variables.rearrange[i].lower()== "Them".lower() or variables.rearrange[i].lower()== "Their".lower() or variables.rearrange[i].lower()== "We".lower() or variables.rearrange[i].lower()== "Our".lower() or variables.rearrange[i].lower()== "Us".lower():
                    variables.multi.append("p")
        else:
            variables.multi.append(-1)
        i=i+1

# print(variables.multi)

def degree_list():
    i=0
    while i<len(variables.rearrange): # to identify degree of tokens
        if variables.pos[i]== "NN" or variables.pos[i]== "NNP" or variables.pos[i]== "NNPS" or variables.pos[i]== "NNS":
            variables.degree.append(3)
        elif variables.pos[i]== "PRP" or variables.pos[i]== "PRP$":
            if variables.rearrange[i].lower()== "I".lower() or variables.rearrange[i].lower()== "Me".lower() or variables.rearrange[i].lower()== "My".lower() or variables.rearrange[i]== "Mine".lower() or variables.rearrange[i].lower()== "We".lower() or variables.rearrange[i].lower()== "Our".lower() or variables.rearrange[i].lower()== "Us".lower():
                variables.degree.append(1)
            elif variables.rearrange[i].lower()== "You".lower() or variables.rearrange[i].lower()== "Your".lower() or variables.rearrange[i].lower()== "Yours".lower():
                variables.degree.append(2)
            elif variables.rearrange[i].lower()== "He".lower() or variables.rearrange[i].lower()== "She".lower() or variables.rearrange[i].lower()== "It".lower() or variables.rearrange[i]== "They".lower() or variables.rearrange[i].lower()== "His".lower() or variables.rearrange[i].lower()== "Him".lower() or variables.rearrange[i].lower()== "Her".lower() or variables.rearrange[i].lower()== "Them".lower() or variables.rearrange[i].lower()== "Their".lower():
                variables.degree.append(3)
        else:
            variables.degree.append(-1)
        i=i+1


#print(variables.degree)

