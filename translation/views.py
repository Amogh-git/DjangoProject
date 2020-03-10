from django.shortcuts import render
from django.contrib import messages
from nltk import word_tokenize
from translation.forms import InputForm
from translation import variables, parsing, reorder, grammar_metadata, gender_identification, vibhakti_identification, \
    translate

eng1 = open("agro1.english", "r", encoding="utf-8").readlines()
eng2 = open("agro2.English", "r", encoding="utf-8").readlines()
eng3 = open("agro3.English", "r", encoding="utf-8").readlines()
mar1 = open("agro1.Marathi", "r", encoding="utf-8").readlines()
mar2 = open("agro2.Marathi", "r", encoding="utf-8").readlines()
mar3 = open("agro3.Marathi", "r", encoding="utf-8").readlines()
ans = ""
flag = 0
loading = 0


def home(request):
    global ans, flag, loading
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            messages.success(request, "loading...")
            ext = form.cleaned_data
            para = ext.get("inputText")
            lines = para.split(".")
            ans = ''
            for i in lines:
                if i == '':
                    break
                variables.sentence = i
                init()
                print('--------parsing ', i)
                flag = 0
                loading = 1
                parsing.parse()
                parsing.traverse_tree(variables.root)

                print("------reordering for ", i)
                reorder.token(variables.root)

                grammar_metadata.remove_DT()
                print("English list:", variables.english)
                print("Rearranged tokens:", variables.rearrange)

                print("-----grammer metadata tense identification")
                grammar_metadata.tense_identification()
                print("tense is:", variables.tense1)

                print("------grammer metadata pos_list=")
                grammar_metadata.pos_list()
                print(variables.rearrange)
                print("Rearranged POS:", variables.pos)

                print("grammer metadata multi list")
                grammar_metadata.multi_list()
                print("Multiplicity:", variables.multi)

                print("-------grammer metadata degree")
                grammar_metadata.degree_list()
                print("degree:", variables.degree)

                print("------grammer identification gender")
                gender_identification.gender_list()
                print("gender:", variables.gender)

                print("------viibhakti identification case list")
                vibhakti_identification.case_list()
                print("case is:", variables.case)
                print("dependency is", variables.dependency)
                x = findsentence(i)
                ans = ans + x
                """print('translation is')
                translate.marathi_list()
                print("Lexicons are:", variables.lexicon)
                print("Trans. marathi words:", variables.marathi)"""
            flag = 1
            loading = 0
            return render(request, "home.html", {'form': form, 'ans': ans, 'flag': flag, 'loading': loading})
        else:
            print("invalid")
    else:
        form = InputForm()
        flag = 0
        loading = 0
    return render(request, "home.html", {'form': form, 'ans': ans, 'flag': flag, 'loading': loading})


def init():
    variables.root = ""
    variables.s1 = ''
    # variables.english = []
    reorder.a = []
    reorder.b = reorder.c = ''
    variables.degree = []
    variables.multi = []
    variables.gender = []
    variables.case = []
    variables.dependency = []
    variables.lexicon = []
    variables.marathi = []


def findsentence(sentence):
    global ans
    start = 0
    for line in eng1:
        if line[:-2] == sentence:
            # ans = mar2[sta
            return mar1[start]
        else:
            start = start + 1
    start = 0
    for line in eng2:
        if line[:-2] == sentence:
            # ans = mar2[sta
            return mar2[start]
        else:
            start = start + 1
    start = 0
    for line in eng3:
        if line[:-2] == sentence:
            # ans = mar2[sta
            return mar3[start]
        else:
            start = start + 1
