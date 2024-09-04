import pandas as pd
import numpy as np
import csv
import re

data = pd.read_csv("../data/phase2_baby_group3.csv",index_col=0)

asin_url = "http://amazon.com/dp/"

def sent_tokenize(text):
    """Adapted from https://stackoverflow.com/a/5802300
    """
    delim = ".?!"
    top_level_domains = r"\.(?:com|org|co\.uk|org|edu|net|ca|de)"
    abbrev = "(?:mr|ms|mrs|vs|dr|i\.? ?e)\."

    regex = re.compile(r"(?:\d[\)\.])?"
                       r"(?:"
                            r"\b{2}|"
                            r"[^{0}0-9]|"
                            r"{1}|"
                            r"\d(?![\)\.])|"
                            r"(?<=[^a-z{0}:;])\d[\).]|"
                            r"\d\.\d|"
                            r"\. *[,-]"
                            r"\W+[,-]"
                        r")+"
                        r"(?:"
                            r"[{0}]*[ {0}\)]*['\"]*|"
                            r"(?=\Z)"
                        r")|"
                        r"[{0}][ {0}]*".format(delim,top_level_domains,abbrev), re.IGNORECASE)

    res = regex.findall(text)
    return [r.strip() for r in res]

with open('sentences_2.csv','w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['reviewID','sentenceID', 'productLink', 'sentenceText', 'polarity', 'notes'])
    for i, row in data.iterrows():
        productLink =  asin_url + row['asin']
        sentences = sent_tokenize(row["reviewText"].strip())

        for j, sentence in enumerate(sentences):
            writer.writerow([i,j,productLink,'"' + sentence + '"',"",""])
