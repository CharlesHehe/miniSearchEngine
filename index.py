from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
import math


class Index:
    def __init__(self, db):
        self.punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        self.term_dic = {}
        self.document_dic = {}
        self.db = db

    def index_document(self, document):

        for ele in document['text']:
            if ele in self.punctuation:
                document['text'] = document['text'].replace(ele, " ")

        document['text'] = document['text'].lower()
        text_tokens = word_tokenize(document['text'])
        self.document_dic.update({document['id']: len(text_tokens)})
        tokens_without_sw = [word for word in text_tokens if word not in stopwords.words()]
        for term in tokens_without_sw:
            if term not in self.term_dic:
                self.term_dic[term] = {document['id']: 1}
            elif term in self.term_dic:
                if document['id'] in self.term_dic[term].keys():
                    self.term_dic[term][document['id']] += 1
                elif document['id'] not in self.term_dic[term].keys():
                    self.term_dic[term].update({document['id']: 1})

        self.db.add(document)

    def search(self, query):
        if query in self.term_dic.keys():
            tf_idf_dic = self.term_dic[query]
            for i in tf_idf_dic:
                # Term-Frequency and Inverse Document Frequency
                tf_idf_dic[i] = (tf_idf_dic[i] / self.document_dic[i]) * math.log(
                    len(self.document_dic) / len(tf_idf_dic))
                #     sort by tf_idf
            tf_idf_dic = sorted(tf_idf_dic.items(), key=lambda x: x[1], reverse=True)
        return tf_idf_dic
