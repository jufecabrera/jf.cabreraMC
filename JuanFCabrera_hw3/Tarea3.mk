Resultados_hw3.pdf : Resultados_hw3.tex 30.png 60.png orbitas.png
	pdflatex Resultados_hw3.tex 
	rm Resultados_hw3.aux
	rm Resultados_hw3.log
30.png : Onda.py
	python $^
60.png : Onda.py
	python $^
orbitas.png : Plots_Planetas.py
	python $^
Plots_Planetas.py : Planetas.x
	./$^ > planetas.csv
Planetas.x : Planetas.c
	cc $^ -lm -o $@
	
