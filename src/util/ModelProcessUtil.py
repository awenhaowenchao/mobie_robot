import re
import sys
from pyhanlp import *
from bee.ext import files
from pyspark import SparkContext, Row
from pyspark.ml.linalg import Vectors


def load_vocabulary_dict() -> dict:
    vocabulary = {}
    with open("/Users/haowenchao/Downloads/PycharmProjects/movie_robot/src/config/data/vocabulary.txt", "r") as f:
        for line in f.readlines():
            pair = line.strip().split(":")
            vocabulary[pair[1]] = pair[0]
    return vocabulary

vocabulary_dict = load_vocabulary_dict()
_len = len(vocabulary_dict)

def list_all_template():
    result = {}
    for x in files.all_file("/Users/haowenchao/Downloads/PycharmProjects/movie_robot/src/config/data", "*.txt"):
        if x.find("【")>-1:
            r = re.compile("/Users/haowenchao/Downloads/PycharmProjects/movie_robot/src/config/data/【(\d+)】\w+【*\w+】*[.]txt")
            match = r.match(x)
            if match:
                name = match.group(1)
                result[int(name)] = x
    return result

def create_train_vectors():

    vecs = []
    template_files = list_all_template()
    # print(template_files)
    for i, v in template_files.items():
        # print(v)
        with open(v, "r") as file:
            for line in file.readlines():
                # print("-----" + line.strip() + "-------")
                # v = {}
                # for term in HanLP.segment(line.strip()):
                #     # print('{}\t{}'.format(term.word, term.nature))  # 获取单词与词性
                #     if vocabulary_dict.__contains__(term.word):
                #         idx = vocabulary_dict[term.word]
                #         v[int(idx)] = 1
                vec, terms = create_train_vector(line.strip())

                if len(vec) > 0:
                    row = Row(label=i, features=Vectors.dense(*vec))
                del vec
                vecs.append(row)
    return vecs

def create_train_vector(query):
    vec_array = [0] * 190
    terms = HanLP.segment(query)
    for term in terms:
        # print('{}\t{}'.format(term.word, term.nature))  # 获取单词与词性
        if vocabulary_dict.__contains__(term.word):
            idx = vocabulary_dict[term.word]
            vec_array[int(idx)] = 1
    return vec_array, terms


# print(load_vocabulary_dict())
# print(list_all_template())
# print(create_train_vectors())



