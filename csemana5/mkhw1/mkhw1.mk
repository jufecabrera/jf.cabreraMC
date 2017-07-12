all : *.pdf
	
%.pdf : %.py
	python $^
err.pdf : integral.py
	python $^
