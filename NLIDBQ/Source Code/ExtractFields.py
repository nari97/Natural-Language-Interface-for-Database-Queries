import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer


def returnPNNorCD(sent,pncd):
    stop_words = set(stopwords.words('english'))
    stop_words.remove("all")
    stop_words.remove("of")
    stop_words.add("show")
    stop_words.remove("where")
    stop_words.add("equals")

    toke = word_tokenize(sent)
    
    sent = [w for w in toke if not w in stop_words]
    newSent = sent

    i = sent.index("where")
    sent = sent[i:]

    tag = nltk.pos_tag(sent)

    for a in tag:
        if a[1]=="NNP" or a[1] == "CD":
            pncd.append(a[0])

    newSent = [w for w in newSent if not w in pncd]

    sent =""
    for x in newSent:
        sent = sent + x + " "
    
    return sent,pncd

a = []

sent,a = returnPNNorCD("select all from Student where name of teacher is name of student and name of student is Narayanan",a)

print sent
print a
