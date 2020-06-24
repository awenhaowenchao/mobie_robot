from py2neo import Graph,Node

graph = Graph('http://127.0.0.1:7474', username="123456", password="123456")

def get_movie_node_by_name(name) -> Node:
    cypher = 'MATCH (n:Movie) WHERE n.title="' + name + '" RETURN n'
    cursor = graph.run(cypher)
    return cursor.data()[0]['n']

def get_person_node_by_name(name) -> Node:
    cypher = 'MATCH (n:Person) WHERE n.name="' + name + '" RETURN n'
    cursor = graph.run(cypher)
    return cursor.data()[0]['n']




