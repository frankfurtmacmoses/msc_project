import sys
import json
from textblob import TextBlob

def get_stdin():
    file_path = input("enter file path including name & extention: ")

    file = open(file_path,"r")
    buf = file.read()
    return buf

if __name__ == "__main__":
    st = get_stdin()
    blob = TextBlob(st)
    
    res = {
        "polarity": 0,
        "subjectivity": 0
    }

    for sentence in blob.sentences:
        res["subjectivity"] = res["subjectivity"] + sentence.sentiment.subjectivity
        res["polarity"] = res["polarity"] + sentence.sentiment.polarity

    total = len(blob.sentences)

    res["sentence_count"] = total
    res["polarity"] = res["polarity"] / total
    res["subjectivity"] = res["subjectivity"] / total

    print(json.dumps(res))
