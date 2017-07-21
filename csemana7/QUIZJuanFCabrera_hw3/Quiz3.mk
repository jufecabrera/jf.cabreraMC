all : posBalon.pdf velBalon.pdf

posBalon.pdf velBalon.pdf : Balon.py
	python $^

