# BLEU
# 1-gram individual BLEU
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
UnicodeEncodeError('False', 'False', False, False, 'False')
reference = [
    ['this', 'is', 'small', 'test', '.', 'the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']]
candidate = ['this', 'is', 'a', 'test', '.', 'the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
score = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))
print('score 1 ', score)
# 4-gram cumulative BLEU
from nltk.translate.bleu_score import sentence_bleu

reference = [
    ['this', 'is', 'small', 'test', '.', 'the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']]
candidate = ['this', 'is', 'a', 'test', '.', 'the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
score = sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25))
print('score 2', score)
from nltk.translate.bleu_score import sentence_bleu

reference = [['मी', 'सफरचंद', 'खातो/खाते']]
candidate = ['मी', 'सफरचंद', 'खातो/खाते']
score = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))
print('score 3 ', score)
# 4-gram cumulative BLEU
from nltk.translate.bleu_score import sentence_bleu

reference = [['मी', 'सफरचंद', 'खातो/खाते']]
candidate = ['मी', 'सफरचंद', 'खातो/खाते']
score = sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25))
print('score 4 ', score)

reference = [['मी', 'जिंकलो/जिंकले'], ['ते', 'पळाले.'], ['मी', 'पडलो/पडले.'], ['मी', 'ओळखतो/ओळखते'],
             ['मी', 'करतो/करते'], ['आम्ही', 'नाचतो/नाचतो'], ['तू', 'रडतोस/रडतेस'], ['तो', 'चालतो'], ['ती', 'बोलते'],
             ['ते', 'हलते'], ['ते', 'नाचतात/नाचतात'], ['मी', 'करत/करत', 'आहे/आहे'], ['आम्ही', 'नाचत/नाचत', 'आहे/आहे'],
             ['तु', 'रडत/रडत', 'आहे/आहे'], ['तो', 'चालत', 'आहे'], ['ती', 'बोलत', 'आहे'], ['ते', 'हलते', 'आहे'],
             ['ते', 'नाचत/नाचत', 'आहेत/आहेत'], ['त्या', 'नाचत/नाचत', 'आहेत/आहेत'], ['ती', 'बोलते', 'आहे'],
             ['ती', 'बोलत', 'आहे'], ['ते', 'हलते', 'आहे'], ['ते', 'हलत', 'आहे'], ['तू', 'रडतो', 'आहेस'],
             ['तू', 'रडत/रडत', 'आहेस/आहेस'], ['मी', 'बोललो/बोलली'], ['मी', 'नाचलो/नाचले'], ['आम्ही', 'हसलो/हसली'],
             ['तू', 'बसलास/बसलीस'], ['त्या', 'भेटले/भेटल्या'], ['मी', 'चित्र', 'रंगवले'], ['तू', 'चित्र', 'रंगवलेस'],
             ['तू', 'गोष्ट', 'सांगितलीस'], ['तु', 'कथा', 'सांगितलीस/सांगितलीस']]

candidate = ['मी', 'जिंकलो/जिंकले', 'ते', 'पळाले.', 'मी', 'पडलो/पडले.', 'मी', 'ओळखतो/ओळखते', 'मी', 'करतो/करते', 'आम्ही',
             'नाचतो/नाचतो', 'तु', 'रडतोस/रडतेस', 'तो', 'चालतो', 'ती', 'बोलते', 'ते', 'हलवते', 'त्या', 'नाचतात/नाचतात',
             'मी', 'करत/करत', 'आहे/आहे', 'आम्ही', 'नाचत/नाचत', 'आहे/आहे', 'तु', 'रडत/रडत', 'आहे/आहे', 'तो', 'चालत',
             'आहे', 'ती', 'बोलत', 'आहे', 'ते', 'हलवत', 'आहे', 'त्या', 'नाचत/नाचत', 'आहे/आहे', 'ती', 'बोलत', 'आहे', 'ते',
             'हलवत', 'आहे', 'तु', 'रडत/रडत', 'आहे/आहे', 'मी', 'बोललो/बोलले', 'मी', 'नाचलो/नाचले', 'आम्ही', 'स्मित',
             'करलो/स्मित', 'करलो', 'तु', 'बसलास/बसलीस', 'त्या', 'भेटले/भेटल्या', 'मी', 'चित्र', 'रंग', 'देणे/रंग',
             'देणे', 'तु', 'चित्र', 'रंग', 'देणे/रंग', 'देणे', 'तु', 'कथा', 'सांगलास/सांगलीस']

score = sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25))
print("Bleu:", score)
