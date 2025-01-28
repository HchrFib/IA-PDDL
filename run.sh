#!/bin/bash


if [ $# -ne 1 ]; then
  echo "ERROR: you need to provide the name of the example in order to execute it"
else
  ./ff -O -o tareas.pddl -f tests/$1.pddl
fi
