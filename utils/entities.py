# coding: utf-8

from dataclasses import dataclass, field
from pickletools import float8
from typing import List, Union
from uuid import uuid4


__all__ = [
    'Document',
    'Page',
    'Paragraph',
]


@dataclass
class Document:
    file_name: str
    text: str
    cleaned_text: Union[List[str], str] = field(default_factory=str)
    vector: list = field(default_factory=list)
    id: int = field(default_factory=int)

    def __post_init__(self):
        self.id = uuid4().int



@dataclass
class Page:
    file_name: str
    page_number: int
    text: str
    cleaned_text: Union[List[str], str] = field(default_factory=str)
    vector: list = field(default_factory=list)
    id: int = field(default_factory=int)

    def __post_init__(self):
        self.id = uuid4().int


@dataclass
class Paragraph:
    file_name: str
    page_number: str
    paragraph_number: int
    text: str
    cleaned_text: Union[List[str], str] = field(default_factory=str)
    vector: list = field(default_factory=list)
    id: int = field(default_factory=int)

    def __post_init__(self):
        self.id = uuid4().int
