# coding: utf-8

from typing import Callable
from typing import Generator
from pathlib import Path
import pickle

from sklearn.metrics.pairwise import cosine_similarity
import fitz

from app import Pdf
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
        max_output: int = 1000
) -> Generator:

    database: dict

    with open(database_path, 'rb') as file:
        database = pickle.load(file)

    document = create_embedings(
        model=model,
        dataloader=doc_dataloader
    )

    document_path = doc_dataloader._files[0]
    document_filename = document_path.name
    document_fitz = fitz.open(document_path)

    progress_100 = len(document)
    progress_step = 100 // progress_100
    progress = progress_step

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

        similarities.sort(key=lambda e: e['similarity_rate'])

        if similarities:
            page_number = section['page_number'] - 1  # -1 to start count at 0
            coordinates = section['coordinates']
            Pdf.highlight_annot(
                document=document_fitz,
                page_number=page_number,
                coordinates=coordinates,
                content=''
            )

        yield {
            'progress': progress,
            'section': section,
            'similarities': similarities[:max_output],
        }
    document_fitz.save(settings.WORKDIR / f'checked-{document_filename}')


if __name__ == '__main__':
    # model = Doc2vec(load_from='assets/models/model-Doc2vec.pickle')
    model = AllMiniLML6V2()
    database_path = settings.CACHE_FOLDER / f'emdedings-{model}.pickle'
    doc_dataloader = dt(
        filespath=Path('.static/2c770482-doc.pdf'),
        cleaner=cleaner
    )
    predictions = predict_plagiarism(
        model=model,
        database_path=database_path,
        doc_dataloader=doc_dataloader,
        threshold=50
    )
    print(list(predictions))
