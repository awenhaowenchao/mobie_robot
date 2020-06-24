from src.dao import speaker_dao

def get_score_by_movie_name(movie_name) -> float:
    node = speaker_dao.get_movie_node_by_name(movie_name)
    return node.get("rating")

def get_releasedata_by_movie_name(movie_name) -> float:
    node = speaker_dao.get_movie_node_by_name(movie_name)
    return node.get("releasedate")


def get_birthday_by_person_name(person_name):
    node = speaker_dao.get_person_node_by_name(person_name)
    return node.get("birth")