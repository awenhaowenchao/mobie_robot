import os

from pyspark import SparkContext, Row
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.linalg import Vectors
from pyspark.shell import spark
from pyspark.ml import PipelineModel
from src.api import speaker


from src.util import ModelProcessUtil

# sc = SparkContext.getOrCreate()



def main():
    print("create_classifier_model")
    # 训练问题模板模型
    model = load_classifier_model()
    # vec_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # vTest = Vectors.dense(*vec_array)
    # test0 = sc.parallelize([Row(features=vTest)]).toDF()
    #
    #
    # model_index = model.predict(test0.head().features)
    # print(model.predictProbability(test0.head().features))
    # print("标签分类编号：%s" % model_index)

    print("start speaker...")
    speaker.run(model)

def load_classifier_model():
    # model = PipelineModel.load("./movie-robot-model")
    # print(model)
    # if model != None:
    #     return model


    data_set = ModelProcessUtil.create_train_vectors()

    df = spark.createDataFrame(data_set)

    df.show()
    nb = NaiveBayes(modelType="bernoulli")
    nb_model = nb.fit(df)
    nb_model.setFeaturesCol("features")
    # nb_model.save("./movie-robot-model")
    nb_model.write().overwrite().save("./movie-robot-model")

    return nb_model

if __name__ == '__main__':
    main()