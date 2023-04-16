help:
	@echo "make help            	- Prints this help message"
	@echo "make flake8				- Run linting check with flake8"
	@echo "make test            	- Runs automated test suite"
	@echo "make train            	- Train all models"
	@echo "make embediddings        - create embeddings"
	@echo "make streamlit-server    - Run streamlit"
	

flake8:
	flake8 app

test: export TEST=1
test:
	pytest

train:
	python train.py

embediddings:
	python embeddings.py

streamlit-server:
	streamlit run streamlit.py
