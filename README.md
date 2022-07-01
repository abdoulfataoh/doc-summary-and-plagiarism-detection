### Description
In this project, we use deeplearning models to detect plagiarism and summarize documents

### Configuration

We use poetry for create virtual environement and python dependencies management
- ```sudo apt-get update && sudo apt-get install poetry``` to install poetry on linux
- ```poetry install``` to enable all project dependencies
- ```poetry shell``` to enable the project virtual environement
 
### Pdf module
The pdf module [(utils/pdf)](https://github.com/abdoulfataoh/doc-summary-and-plagiarism-detection/blob/main/utils/pdf.py) can extract text from pdf files with **"paragraph"**, **"page"**, **"document"** as granulaties options

<p align="left">
  <img width="500" src="https://drive.google.com/uc?export=download&id=1Cx1TngBWoMn92GF9voF6ZHVbkhhKcfzh">
</p>

### DataLoader module
Le module DataLoader charge tous les jeux de données (*.pdf) à partir d'un dossier contenant des fichiers pdf. Il utilise d'abord le module pdf pour extraire le texte de tous les fichiers pdf, ensuite il utilise le module Tokenize de nlp_tool.py pour la tokenisation, la suppression des mots vides, enfin il contient des méthodes statiques pour le balisage des documents.

### General artichecture

