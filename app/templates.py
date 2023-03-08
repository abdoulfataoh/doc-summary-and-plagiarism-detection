# coding: utf-8

from dataclasses import dataclass, field
from typing import List, Union
from uuid import uuid4


__all__ = [
    'Document',
    'Page',
    'Paragraph',
]


@dataclass
class Document:
    filename: str
    text: str
    cleaned_text: Union[List[str], str] = field(default_factory=str)
    vector: list = field(default_factory=list)
    id: int = field(default_factory=int)

    def __post_init__(self):
        self.id = uuid4().hex

    @staticmethod
    def to_dict(**kwargs) -> dict:
        document = Document(**kwargs)
        return document.__dict__


@dataclass
class Page:
    filename: str
    page_number: int
    text: str
    cleaned_text: Union[List[str], str] = field(default_factory=str)
    vector: list = field(default_factory=list)
    id: int = field(default_factory=int)

    def __post_init__(self):
        self.id = uuid4().hex

    @staticmethod
    def to_dict(**kwargs) -> dict:
        page = Page(**kwargs)
        return page.__dict__


@dataclass
class Paragraph:
    filename: str
    page_number: str
    paragraph_number: int
    text: str
    coordinates: tuple = field(default_factory=tuple)
    cleaned_text: Union[List[str], str] = field(default_factory=str)
    vector: list = field(default_factory=list)
    id: int = field(default_factory=int)

    def __post_init__(self):
        self.id = uuid4().hex

    @staticmethod
    def to_dict(**kwargs) -> dict:
        paragraph = Paragraph(**kwargs)
        return paragraph.__dict__
