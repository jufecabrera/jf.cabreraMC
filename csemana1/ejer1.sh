#despues de descargar signif.txt
awk -F "\t" '{print $21, $22;}' signif.txt > coordenadas.txt 
awk '{print $1;}' coordenadas.txt > Lat.txt
awk '{print $2;}' coordenadas.txt > Long.txt
