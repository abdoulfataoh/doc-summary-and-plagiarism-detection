<p>
  <img src="https://github.com/abdoulfataoh/doc-summary-and-plagiarism-detection/actions/workflows/test-workflow.yaml/badge.svg">
  <img src="https://img.shields.io/badge/version-1.0.1-brightgreen">
  <img src="https://img.shields.io/badge/-DEEPLEARNING-blue">
  <img src="https://img.shields.io/badge/-PLAGIARISM%20DECTECTION-orange">
  <img src="https://img.shields.io/badge/-DOCUMENT%20SUMMARY-red">
</p>


### Description
In this project, we use deep learning models for the purpose of plagiarism detection and document summarization.
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
```bash
  python -m spacy download en_core_web_sm
  python -m spacy download fr_core_news_sm
  python -m nltk.downloader punkt
```

- (optional) Use test configuration and file
```bash
  echo -n 'TEST=True' > .env
  make flake8
  make test
```

### Settings
The configuration of the system is done through configuration variables. 
```export``` command can be used to set a variable value. For example:
```bash
  export TEST=True  # To enable test mode
```
  
Settings  | Description
------------- | -------------
OPENAI_API_KEY  | Your openai api key to interact with chatgpt model
TEST  | if True test mode is enabled else prod mode
WORKDIR  | workdir path
PLAGIARISM_TRAIN_DATASET_FOLDER  | PDFs dataset folder path

### Workflows

#### Plagiarism detection

- Train
![train](https://github.com/abdoulfataoh/doc-summary-and-plagiarism-detection/blob/main/docs/plagiarism_train.png)

- Create embeddings
![embeddings](https://github.com/abdoulfataoh/doc-summary-and-plagiarism-detection/blob/main/docs/plagiarism_embeddings.png)

- Predict
![predict](https://github.com/abdoulfataoh/doc-summary-and-plagiarism-detection/blob/main/docs/plagiarism_predict.png)


#### Summarize
...

### Usage with streamlit

0. (if TEST env is True) Set it to False
```bash
  rm .env
```

1. Train models
> Dataset must be pdf files and stored in ```assets/dataset/plagiarism/train/```
```bash
  make train
```

2. Create embeddings
```bash
  make embeddings
``` 

3. Run the streamlit server to use the app
```bash
  make streamlit-server
```

![streamlit](https://github.com/abdoulfataoh/doc-summary-and-plagiarism-detection/blob/main/docs/streamlit.png)


