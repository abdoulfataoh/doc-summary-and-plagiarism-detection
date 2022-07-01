### Description
In this project, we use deeplearning models to detect plagiarism and summarize documents

### Configuration

We use poetry for creation virtual environement and python dependencies management
- ```sudo apt-get update && sudo apt-get install poetry``` to install poetry on linux
- ```poetry install``` to enable all project dependencies
- ```poetry shell``` to enable the project virtual environement
 
### Pdf module
The pdf module [(utils/pdf)](https://github.com/abdoulfataoh/doc-summary-and-plagiarism-detection/blob/main/utils/pdf.py) can extract text from pdf files with **"paragraph"**, **"page"**, **"document"** as granulaties options

<p align="left">
  <img width="500" src="https://drive.google.com/uc?export=download&id=1Cx1TngBWoMn92GF9voF6ZHVbkhhKcfzh">
</p>

### DataLoader module
The DataLoader module load all dataset (*.pdf) from a folder that contain pdf files. It use the Tokenizer from nlp_tool.py to tokenize and clean stopwords and return 
