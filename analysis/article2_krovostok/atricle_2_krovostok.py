import os
import string
import glob
import pandas as pd

album1_files = glob.glob('raw_data/article_2_krovostok/reka_krovi_2004/./*.txt')

album2_files = glob.glob('raw_data/article_2_krovostok/skvoznoe_2006/./*.txt')

album3_files = glob.glob('raw_data/article_2_krovostok/gantelya_2008/./*.txt')

album4_files = glob.glob('raw_data/article_2_krovostok/studen_2012/./*.txt')

album5_files = glob.glob('raw_data/article_2_krovostok/lombard_2015/./*.txt')

album1_words, album2_words, album3_words, album4_words, album5_words = [], [], [], [], []

for f in album1_files:
    data = open(f, 'r').read()
    exclude = set(string.punctuation)
    s = ''.join(ch for ch in data if ch not in exclude)
    s = s.replace('\n', ' ').lower()
    words = s.split()
    album1_words.extend(words)

