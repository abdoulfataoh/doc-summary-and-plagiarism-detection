# coding: utf-8


from sentence_transformers import SentenceTransformer


class AllMiniLML6V2():
    def __init__(self) -> None:
        pass

    def get_model(self):
        model =  SentenceTransformer("all-MiniLM-L6-v2")
        return model
