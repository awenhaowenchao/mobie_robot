#movie-robot

    movie-robot是一个基于py-auxo-bee、neo4j、hanlp、朴素贝叶斯的伯努利模型构建的基于电影知识图谱的问题系统demo。
    
    核心逻辑及参考训练数据，来自于https://blog.csdn.net/appleyk/article/details/80422055文章。
    
##启动类
    movie_robot/src/main.py
    
##配置文件
    movie_robot/src/config/app.yml
    
    server:
      port: 8585                    web端口号
      context-path: /movie-robot    类似java的context-path
    
    debug: true                     是否debug模式
    banner: true                    是否显示代码神兽
    
    bee:                            本项目暂时没用
      application:
        name: "ml-movie-robot"
        
##访问地址
    http://domain:8585/movie-robot
    
    例如：http://localhost:8585/movie-robot/ask?query=章子怡的生日是多少
    例如：http://localhost:8585/movie-robot/ask?query=卧虎藏龙的评分是多少
    
##neo数据
    https://pan.baidu.com/s/1QJRS8eyZXQt44wBwNyZ6eQ