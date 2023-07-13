import nltk
from nltk.corpus import stopwords

with open("miracle_in_the_andes.txt","r",encoding='utf-8') as file:
    book = file.read()


pattern = re.compile("[a-zA-z]+")
findings = re.findall(pattern, book.lower())
findings[:5]

d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value,key) for (key,value) in d.items()]
d_list = sorted(d_list,reverse=True)
d_list[:5]





english_stopwords =stopwords.words("english")
english_stopwords
