all:
	jupyter nbconvert --to html --output-dir static/html/ notebooks/*.ipynb
