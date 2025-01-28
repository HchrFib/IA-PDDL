import subprocess
import random
import sys

def run_test(num_tasks, num_programmers, optimization_goal, ponderation=None):
    # Generamos el archivo de problema
    subprocess.run(["python3", "problemgenerator.py", str(num_tasks), str(num_programmers), str(optimization_goal), str(ponderation)])

    # Ejecutamos el archivo de prueba con Fast Forward
    subprocess.run(["./run.sh", "gen"])


def errorArgv ():
    print("[ERROR] Missing arguments to problem file creator problems:")
    print("   1) Number of tasks")
    print("   2) Number of programmers")
    print("   3) Optimization goal:")
    print("         1: minimize total time")
    print("         2: minimize ponderated sum of total time and programmers working")
    print("   4) ONLY IF OPTIMIZATION CRITERIA IS 2: ponderation for total work time")
    exit()

def run_experiments():
    
    workers = 0  # numero inicial de programadores
    optimization_goal = 1 # Objetivo de la optimizacion
                           # 1: minimiza el tiempo total
                           # 2: minimizar la suma ponderada de tiempo total y programadores trabajando
    ponderation = 0.2   # Ponderación para el tiempo total de trabajo


    anterior = 0  # Inicializamos la variable anterior con 0
    num_previous_workers = 0
    num_previous_tasks= 0
    i = 1

    while i < 20:
        num_tasks = random.randint(num_previous_tasks + 1, num_previous_tasks + 2)  # Genera un número entero aleatorio mayor que el anterior
        num_workers = random.randint(num_previous_workers + 1, num_previous_workers + 3)  # Genera un número entero aleatorio mayor que el anterior
        num_previous_workers = num_workers
        num_previous_tasks = num_tasks  # Actualizamos el valor de la variable num_previuous_tasks
        
        if(num_workers >= num_tasks):

            print("Iteracion:")
            print(f"Experimentando con {num_tasks} tareas y {num_workers} programadores...;)")
            run_test(num_tasks, num_workers, optimization_goal, ponderation)
            print()
            i += 1


run_experiments()