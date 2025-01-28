(define (problem prueba_basico)
  (:domain tareas)
  ;; LIMITS: T <= P and if there is a task with difficulty 3 there must be at least
  ;;         min{2, #T_difficulty_3+1} programmers with skill 2 or more
  (:objects t1 t2 t3 t4 - task
            p1 p2 p3 p4 - programmer)
  (:init
    (= (difficulty t1) 2)
    (= (difficulty t2) 2)
    (= (difficulty t3) 3)
    (= (difficulty t4) 3)

    (= (skill p1) 1)
    (= (skill p2) 2)
    (= (skill p3) 3)
    (= (skill p4) 2)

    (= (quality p1) 1)
    (= (quality p2) 2)
    (= (quality p3) 1)
    (= (quality p4) 2)

    (= (total_work) 0)          ;; SIEMPRE NECESARIO
    (= (programmers_working) 0) ;; SIEMPRE NECESARIO
  )
  (:goal (forall (?t - task) (and (assigned ?t) (not (to_revise ?t)))))
  (:metric minimize (total_work)) ;; PREGUNTA: me lo ignora xd
  ;;(:metric minimize (+ (* 1 (total_work)) (* 1 (programmers_working))))
)
