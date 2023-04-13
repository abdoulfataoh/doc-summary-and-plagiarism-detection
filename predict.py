# coding: utf-8

from typing import Callable
from typing import Generator
from pathlib import Path
import pickle

from sklearn.metrics.pairwise import cosine_similarity

from app import pdf
from app import cleaner
from app import settings
from embeddings import create_embedings
from app.dataloader import DataLoader as dt
from app.models.plagiarism.base import PlagiarismModelInterface as plagiarism_model # noqa:
from app.models.plagiarism import Doc2vec  # noqa: F401
from app.models.plagiarism import AllMiniLML6V2  # noqa: F401


def predict_plagiarism(
        model: plagiarism_model,
        database_path: Path,
        doc_dataloader: dt,
        similarity_function: Callable = cosine_similarity,
        threshold: int = 50,
) -> Generator:

    database: dict

    with open(database_path, 'rb') as file:
        database = pickle.load(file)

    document = create_embedings(
        model=model,
        dataloader=doc_dataloader
    )

    progress = 0
    progress_100 = len(document)
    progress_step = progress_100 // 100

    for section in document:
        similarities: list = []
        for data in database:
            result = similarity_function(
                section['embeding'].reshape(1, -1),
                data['embeding'].reshape(1, -1)
            )
            result = result[0][0] * 100
            result = int(result)
            if result >= threshold:
                data['similarity_rate'] = result
                data_copy = data.copy()
                del data_copy['embeding']
                similarities.append(data_copy)
        del section['embeding']

        progress = progress + progress_step
        progress = progress if progress <= 100 else 100
        
        yield {
            'progress': progress,
            'section': section,
            'similarities': similarities,
        }


if __name__ == '__main__':
    # model = Doc2vec(load_from='assets/models/model-Doc2vec.pickle')
    model = AllMiniLML6V2()
    database_path = settings.EMBEDDINGS_FOLDER / f'emdedings-{model}.pickle'
    doc_dataloader = dt(
        filespath=Path('workdir/doc.pdf'),
        pdf=pdf,
        cleaner=cleaner
    )
    predictions = predict_plagiarism(
        model=model,
        database_path=database_path,
        doc_dataloader=doc_dataloader,
        threshold=50
    )
    print(list(predictions))
