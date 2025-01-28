(define (problem prueba_basico)
  (:domain tareas)
  (:objects t1 t2 - task
            p1 p2 p3 - programmer)
  (:init

     (= (difficulty t1) 3)
     (= (difficulty t2) 3)

     (= (skill p1) 3)
     (= (skill p2) 1)
     (= (skill p3) 3)

     (= (quality p1) 2)
     (= (quality p2) 1)
     (= (quality p3) 2)

     (= (total_work) 0)
     (= (programmers_working) 0)
)
  (:goal (forall (?t - task) (and (assigned ?t) (not (to_revise ?t)))))
  (:metric minimize (total_work))
)