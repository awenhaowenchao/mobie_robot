from bee.net.web_flask import bapp
from flask import request
from pyspark import SparkContext, Row
from pyspark.ml.linalg import Vectors
from src.biz import speaker_biz

from src.util import ModelProcessUtil


@bapp.route('/welcome', methods=['GET'])
def welcome():
    s = '<h1 style="font-color:red">Welcome access to movie robot!</h1>'
    return s

@bapp.route('/ask', methods=['GET'])
def ask():
    query = request.args.get("query")
    model_index, terms = match_template(query)
    return switch_process(model_index, query, terms)



def run(nb_model):
    global model
    model = nb_model
    from bee.net.web_flask.server import start_up
    start_up()



def match_template(query):
    # for term in HanLP.segment(query):
    #     print('{}\t{}'.format(term.word, term.nature))  # 获取单词与词性
    vec_array, terms = ModelProcessUtil.create_train_vector(query)
    vTest = Vectors.dense(*vec_array)
    sc = SparkContext.getOrCreate()
    test0 = sc.parallelize([Row(features=vTest)]).toDF()

    model_index = model.predict(test0.head().features)
    print(model.predictProbability(test0.head().features))
    print("标签分类编号：%s" % model_index)
    return model_index, terms

def process_0(query, terms):
    print("评分：" + query)
    movie_name = ''
    for term in terms:
        print('{}\t{}'.format(term.word, term.nature))  # 获取单词与词性
        if str(term.nature) == "nz" or str(term.nature) == "nm" or str(term.nature) == "n":
            movie_name =term.word
            break
    score = speaker_biz.get_score_by_movie_name(movie_name)
    print("score=%s, type=%s" % (score, type(score)))
    return "{}'s score is {}".format(movie_name, score)
    #与neo交互

def process_1(query, terms):
    print("评分：" + query)
    movie_name = ''
    for term in terms:
        print('{}\t{}'.format(term.word, term.nature))  # 获取单词与词性
        if str(term.nature) == "nz" or str(term.nature) == "nm" or str(term.nature) == "n":
            movie_name =term.word
            break
    releasedata = speaker_biz.get_releasedata_by_movie_name(movie_name)
    print("releasedate=%s, type=%s" % (releasedata, type(releasedata)))
    return "{}'s releasedata is {}".format(movie_name, releasedata)
def process_13(query, terms):
    print("生日：" + query)
    person_name = ''
    for term in terms:
        print('{}\t{}'.format(term.word, term.nature))  # 获取单词与词性
        if str(term.nature) == "nr":
            person_name =term.word
            break
    birthday = speaker_biz.get_birthday_by_person_name(person_name)
    print("releasedate=%s, type=%s" % (birthday, type(birthday)))
    return "{}'s releasedata is {}".format(person_name, birthday)

def switch_process(model_index, query, terms):
    if model_index == 0.0:
        return process_0(query, terms)
    elif model_index == 1.0:
        return process_1(query, terms)
    elif model_index == 13.0:
        return process_13(query, terms)

