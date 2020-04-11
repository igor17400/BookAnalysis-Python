# Markov analysis, for a given sequence of words, ig give us the probability of the words 
# that might come next

import re
import string

suffix_dic = {}
pefix_tup = ()

def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)

def file_words(file):
    data = file.read()
    list = re.findall(r"[\w']+|[.,!?;]", data)

    return list 


def creating_dict(list):
    global pefix_tup
    for j in range(len(list)):
        if list[j] not in string.punctuation:
            if(list[j] == 'END'):
                break

            if(len(pefix_tup) < 2):
                pefix_tup += (list[j],)
                continue
            try:
                suffix_dic[pefix_tup].append(list[j])
            except KeyError:
            # if there is no entry for this prefix, make one
                suffix_dic[pefix_tup] = [list[j]]

        pefix_tup = shift(pefix_tup, list[j])

fin = open('book/sample.txt')
lista = file_words(fin)
creating_dict(lista)
print(suffix_dic)

