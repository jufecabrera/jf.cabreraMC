PuntoNemo.pdf : Plots.py
	python $^
Plots.py : a.out
	./$^
a.out : PuntoGeographicPoint.c
	cc $^ -lm
