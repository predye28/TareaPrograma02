#!/usr/bin/env python3

import sys
import csv
import nltk
from nltk.stem import SnowballStemmer

nltk.download("stopwords")
stemmer = SnowballStemmer("spanish")

def process_page(row):
    if row["Page_Title"] != "Page_Title":  # Skip header
        page_title = row["Page_Title"]
        words = nltk.word_tokenize(row["Subtitle_Text"])
        stemmed_words = set([stemmer.stem(word.lower()) for word in words if word.isalpha()])
        
        for word in stemmed_words:
            print(f"{page_title}\t1")

def main():
    csv_reader = csv.DictReader(sys.stdin)
    for row in csv_reader:
        process_page(row)

if __name__ == "__main__":
    main()


