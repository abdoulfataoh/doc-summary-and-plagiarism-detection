# coding: utf-8

import torch
from transformers import RobertaTokenizerFast, EncoderDecoderModel


class Camembert2camembert_shared:
    def __init__(self) -> None:
        ...
    
    def get_model(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        ckpt = 'mrm8488/camembert2camembert_shared-finetuned-french-summarization'
        tokenizer = RobertaTokenizerFast.from_pretrained(ckpt)
        model = EncoderDecoderModel.from_pretrained(ckpt).to(device)
        return model, tokenizer, device
