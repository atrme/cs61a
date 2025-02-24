;;****** Fall 2019 Final Q9: Macro Lens ******
(define-macro (partial call)
    `(lambda (y) ,(append call (list 'y)))
)

;;****** Summer 2019 Final Q10c: Slice ******
(define-macro (slice f at k)
    `(lambda (i) ,(list f `(+ i ,k)))
)

;;****** Spring 2019 Final Q8: Macros ******
(define-macro (if-macro predicate expression alternative)
    `(or 
        ,(list `and predicate expression) 
        ,alternative
    )
)
