### Description
In this project, we employ deep learning models for the purpose of plagiarism detection and document summarization.
### Config

- Clone the project
```bash
  git clone https://github.com/abdoulfataoh/doc-summary-and-plagiarism-detection.git
  cd doc-summary-and-plagiarism-detection
```

- Install poetry for virtual environment management
```bash
  sudo apt-get update
  sudo apt-get install curl
  curl -sSL https://install.python-poetry.org | python3 -
```

- Install dependancies with poetry and use virtual env
```bash
  poetry install --dev
  poetry shell
```

- Install Spacy and NLTK language models
``bash
  python -m spacy download en_core_web_sm
  python -m spacy download fr_core_news_sm
  python -m nltk.downloader punkt
``

- (optional) Use test configuration and file
```bash
  echo -n 'TEST=True' > .env
  make flake8
  make test
```

### Workflows

#### - Plagiarism detection
![embeddings](https://github.com/abdoulfataoh/doc-summary-and-plagiarism-detection/blob/main/docs/embeddings.png)