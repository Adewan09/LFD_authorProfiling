### Only for dutch dir and for binary gender classification

import os
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import re

maindir = os.getcwd()
dutchdir = os.path.join(maindir,'training/dutch')

os.chdir(dutchdir)

files = os.listdir(dutchdir)

author_tweets = []
author_tags = []
authorids = []
f_index = -1

for f in files:
    if f.lower().endswith(('xml')):
        tweets = []
        tags = []
        fxml = open(f, 'rb')
        tree = ET.parse(fxml)
        root = tree.getroot()
        authorids.append(root.attrib['id'])
        f_index = f_index + 1
        for t in range(len(root)):
            # Pre-processing
            sansusers = re.sub(r"(?:\@|https?\://)\S+","",root[t].text)
            sansurl = re.sub(r'http\S+','',sansusers)
            tags.append({tag.strip("#") for tag in sansurl.split() if tag.startswith("#")})
            tweets.append(sansurl)
        author_tweets.append((authorids[f_index],tweets))
        author_tags.append((authorids[f_index],tags))
        
#author_tweets[author index][1][tweet indices] gives one of the multiple tweets
#author_tweets[author index][0] gives author id
