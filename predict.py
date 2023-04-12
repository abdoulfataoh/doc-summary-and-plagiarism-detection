# coding: utf-8

from typing import Callable
from typing import Generator
from pathlib import Path
import pickle

from sklearn.metrics.pairwise import cosine_similarity
from app.settings import Granularity as G
from embeddings import create_embedings
from app.dataloader import DataLoader as dt
from app.models.plagiarism.base import PlagiarismModelInterface as plagiarism_model # noqa: 


def predict_plagiarism(
        model: plagiarism_model,
        database_path: Path,
        dataloader: dt,
        similarity_function: Callable = cosine_similarity,
        threshold: int = 50,

    ) -> Generator:

    database: dict

    with open(database_path, 'rb') as file:
        database = pickle.load(file)

    document = create_embedings(
        model=model,
        dataloader=dataloader
    )

    for section in document:
        similarities = []
        for data in database:
            result = similarity_function(section['embeding'], data['embeding'])
            result = result * 100
            if result >= threshold:
                similarities.append(data)
        yield {
            'section': section,
            'similarities': similarities,
        }
