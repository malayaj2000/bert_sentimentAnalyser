import ktrain
import nltk
nltk.download('stopwords')
import re
def sentiment(data):
    predictor = ktrain.load_predictor('model')
    res=predictor.predict(data)
    prob=predictor.predict_proba(data)
    print ("sentiment is "'{}'" with a confidence of {:.3f}%".format(res,prob[1]*100))
def remove_stopword_and_stemming(text):
    from nltk.corpus import stopwords
    from nltk.stem.snowball import SnowballStemmer
    sb=SnowballStemmer( language='english')
    stopWord=stopwords.words('english')
    stopWord.remove('not')
    text = text.split()
    r=[sb.stem(word) for word in text if word not in set(stopWord)]
    r=" ".join(r)
    return r
def clean(data):
    data.lower()
    data = re.sub("'", ' ', data)
    data = re.sub(r'[^a-zA-Z0-9]', " ", data)
    data = remove_stopword_and_stemming(data)
    return data
if __name__=="__main__":
    data=input()
    data=clean(data)
    sentiment(data=data)