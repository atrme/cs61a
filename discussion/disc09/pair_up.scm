;;; Return a list of pairs containing the elements of s.
    ;;;
    ;;; scm> (pair-up '(3 4 5 6 7 8))
    ;;; ((3 4) (5 6) (7 8))
    ;;; scm> (pair-up '(3 4 5 6 7 8 9))
    ;;; ((3 4) (5 6) (7 8 9))

(define (first-two s)
    (list (car s) (car (cdr s)))
)
(define (pair-up s)
    (if (<= (length s) 3)
        (list s) 
        ( append (list (first-two s)) (pair-up (cdr (cdr s))) )
    )
)
