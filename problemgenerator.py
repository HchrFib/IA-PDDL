#!/bin/python3

import sys
from random import randint


def genDifficulty (num_tasks, max_difficulty_3):
    line = []
    total_diff_3 = 0
    for i in range(1, num_tasks+1):
        diff = randint(1,2+(total_diff_3 <= max_difficulty_3))
        line.append("     (= (difficulty t"+str(i)+") "+str(diff)+")")
    return "\n".join(line)


def genSkill (num_programmers):
    line = []
    total_skill_3 = 0
    for i in range(1, num_programmers+1):
        skill = randint(1,3)
        if skill == 3:
            total_skill_3 += 1
        line.append("     (= (skill p"+str(i)+") "+str(skill)+")")
    return "\n".join(line), total_skill_3


def genQuality (num_programmers):
    line = []
    for i in range(1, num_programmers+1):
        line.append("     (= (quality p"+str(i)+") "+str(randint(1,2))+")")
    return "\n".join(line)


def errorArgv ():
    print("[ERROR] Missing arguments to problem file generator:")
    print("   1) Number of tasks")
    print("   2) Number of programmers")
    print("   3) Optimization goal:")
    print("         1: minimize total time")
    print("         2: minimize ponderated sum of total time and programmers working")
    print("   4) ONLY IF OPTIMIZATION CRITERIA IS 2: ponderation for total work time")
    exit()


if len(sys.argv) < 4:
    errorArgv()

num_tasks = int(sys.argv[1])
num_programmers = int(sys.argv[2])
line_skill, num_skill_3 = genSkill(num_programmers)
if sys.argv[3] == "1":
    metric_line = "  (:metric minimize (total_work))"
elif sys.argv[3] == "2":
    if len(sys.argv) != 5:
        errorArgv()
    w_time = sys.argv[4]
    w_prog = str(1 - float(w_time))
    metric_line = "  (:metric minimize (+ (* "+w_time+" (total_work)) (* "+w_prog+" (programmers_working))))"
else:
    print("[ERROR] Unknown optimization criteria \""+sys.argv[3]+"\"")
    exit()


file_content = [
    "(define (problem prueba_basico)",
    "  (:domain tareas)",
    "  (:objects " + ' '.join(['t'+str(i) for i in range(1,num_tasks+1)]) + " - task",
    "            " +' '.join(['p'+str(i) for i in range(1,num_programmers+1)]) + " - programmer)",
    "  (:init\n",
    genDifficulty(num_tasks, num_skill_3-1),
    "",
    line_skill,
    "",
    genQuality(num_programmers),
    "",
    "     (= (total_work) 0)",
    "     (= (programmers_working) 0)",
    ")",
    "  (:goal (forall (?t - task) (and (assigned ?t) (not (to_revise ?t)))))",
    metric_line,
    ")"]

file_content = '\n'.join(file_content)

output_file = open("./tests/gen.pddl", "w")
output_file.write(file_content)
output_file.close()
