import re
import string

def file_words(file):
    data = file.read()
    list = re.findall(r"[\w']+|[.,!?;]", data)

    return list 

def histogram_word(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_list(list):
    d = dict()
    for word in list:
        if word not in string.punctuation:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
    return d

def print_bars(num):
    result = ''
    for i in range(num):
        result = result + '-'

    return result
        
def generate_graph(dic):
    for x in dic:
        print(x,': ', print_bars(dic[x]))

def find_ele_dict(dic, num):
    for x in dic:  
        if(dic[x] == num):
            return x 

    return 'None'

def most_freq_words(dic):
    list = []
    
    for x in dic:
        list.append(dic[x])
    
    list = sorted(list)

    print('Top 10 words used in the text')
    for i in range(len(list)-1, len(list)-11, -1):
        print(find_ele_dict(dic, list[i]), ' ==> ', list[i])
    

        

fin = open('book/sample.txt')
list = file_words(fin)
d = histogram_list(list)
print(d)
generate_graph(d)
most_freq_words(d)
