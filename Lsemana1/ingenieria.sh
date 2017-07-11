wget https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv

grep ING 01_notas.tsv | awk '{if(($4 + $5 + $6)/3>=3) print($0);}' > pasaroning.txt

cat pasaroning.txt

grep ING 01_notas.tsv | awk '{if(($4 + $5 + $6)/3>=3) print($0);}'| wc -l | awk '{print("Pasaron", $0, "estudaintes de Ingeniaria");}'

rm 01_notas.tsv

