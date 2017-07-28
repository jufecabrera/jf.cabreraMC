PuntoNemo.pdf : Plots.py
	python $^
	rm m.txt a.out 
Plots.py : a.out
	./$^
a.out : GeographicPoint.c
	cc $^ -lm
