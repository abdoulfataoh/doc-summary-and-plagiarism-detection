help:
	@echo "make help            	- Prints this help message"
	@echo "make flake8				- Run linting check with flake8"
	@echo "make test            	- Runs automated test suite"
	@echo "make streamlit-server    - Run streamlit"
	

flake8:
	flake8 app

test: export TEST=1
test:
	pytest

streamlit-server:
	streamlit run streamlit.py
