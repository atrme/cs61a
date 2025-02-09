(define (remove-parens s)
    (cond
        ( (null? s) nil )
        ( (list? (car s)) 
            (append (remove-parens (car s)) (remove-parens (cdr s)))
        )
        ( else (cons (car s) (remove-parens (cdr s))) )
    )
)

(define (make-necklace beads length)
    (if (= length 1)
        (list (car beads))
        (cons (car beads)
            (make-necklace
             (append (cdr beads) (list(car beads))) 
             (- length 1)
            )
        )
    )
)

