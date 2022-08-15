# coding: utf-8


from sentence_transformers import SentenceTransformer


class CamembertLarge():
    def __init__(self) -> None:
        pass

    def get_model(self):
        model =  SentenceTransformer("camembert/camembert-large")
        return model
