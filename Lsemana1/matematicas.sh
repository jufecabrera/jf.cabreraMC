wget https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv

awk '{if(($4 + $5 + $6)/3>=3 && $3 =="MATEMA") print($0);}' 01_notas.tsv > pasaron.txt

cat pasaron.txt

awk '{if(($4 + $5 + $6)/3>=3 && $3 =="MATEMA") print($0);}' 01_notas.tsv | wc -l | awk '{print("Pasaron", $0, "estudaintes de Matematicas");}'

rm 01_notas.tsv
