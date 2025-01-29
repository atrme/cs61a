(define with-list
    (list
        (list 'a 'b)
        'c
        'd
        (list 'e)
    )
)
; (draw with-list) 


(define with-quote
    '(
        '(a b)
        c
        d
        '(e)
    )
)
; (draw with-quote)


(define first
    (cons 'a (cons 'b nil)))
    
(define with-cons
    (cons
        first
        (cons 'c
        (cons 'd
        (cons (cons 'e nil)
        nil
        )
        )
        )
    )
)
; (draw with-cons)
