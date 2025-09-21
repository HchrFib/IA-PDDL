# IA-PDDL: Práctica de Planificación 

- Fast Forward es un planificador que permite ejecutar planes definidos en el lenguaje PDDL

### Descripción del problema

La idea básica de este problema es hacer una asignación de programadores a tareas de manera automática siguiendo ciertos criterios. Este problema o similares pueden ser comunes en empresas y en algunos casos el tamañoo del problema es tan grande que algoritmos tradicionales no son lo suficientemente potentes para encontrar una solución en tiempo razonable. Más información: [Enunciado de la práctica](PracticaPlanificacion.pdf)

### Ejecución

Para ejecutar el programa:

1. Generar una instancia del problema: generará una instancia llamada "gen.pdll" dentro de la carpeta "test", Es decir, "tests/gen.pddl". Por ejemplo:
``` 
python3 problemgenerator.py 2 3 1
```
- Si ejecutamos el programa de python sin parámetros mostrará instrucciones de uso.

2. Para la ejecutar la instancia generada por el programa python, simplemente hacemos:
```
./run.sh gen
``` 
Ejecutar el programa de python sin parámetros mostrará instrucciones de uso.
