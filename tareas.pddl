(define (domain tareas)
  (:requirements :adl :typing :fluents)
  (:types task programmer - object)
  (:functions
    (difficulty ?t - task)        ;; range (1 2 3)
    (skill      ?p - programmer)  ;; range (1 2 3)
    (quality    ?p - programmer)  ;; range (1 2)
    (total_work) ;; INIT AT ZERO     PREGUNTA: se puede mostrar al final?
                 ;;                            inciar a 0?
    (programmers_working)
  )
  (:predicates
    (assigned ?t - task)
    (programmerdoes ?t -task ?p - programmer)
    (to_revise ?t - task)
    (revise1 ?t - task)
    (revise2 ?t - task)
    (programmer_1_task ?p - programmer)
    (programmer_2_task ?p - programmer)
   )

  (:action task_to_programmer
    :parameters (?t - task ?p - programmer)
    :precondition (and (not (assigned ?t))
                       (not (programmer_2_task ?p))
                       (>= 1 (- (difficulty ?t) (skill ?p))))
    :effect (and (assigned ?t)
                 (programmerdoes ?t ?p)
                 (when (> (difficulty ?t) (skill ?p)) (increase (total_work) 2))
                 (when (= (skill ?p) 1) (revise1 ?t)) ;; PREGUNTA: se puede hacer con fluents?
                 (when (= (skill ?p) 2) (revise2 ?t))
                 (when (programmer_1_task ?p) (programmer_2_task ?p))
                 (when (not (programmer_1_task ?p)) (and (programmer_1_task ?p)
                                                         (increase (programmers_working) 1)))
                 (to_revise ?t))
  )

  (:action revision_to_programmer
    :parameters (?t - task ?p - programmer)
    :precondition (and (to_revise ?t) ;; PREGUNTA: revision cuenta para el numero de tareas?
                       (not (programmerdoes ?t ?p))
                       (not (programmer_2_task ?p))
                       (>= 1 (- (difficulty ?t) (skill ?p))))
    :effect (and (not (to_revise ?t))
                 (when (programmer_1_task ?p) (programmer_2_task ?p))
                 (when (not (programmer_1_task ?p)) (and (programmer_1_task ?p)
                                                         (increase (programmers_working) 1)))
                 (when (revise1 ?t) (increase (total_work) 1))
                 (when (revise2 ?t) (increase (total_work) 2)))
  )
)
