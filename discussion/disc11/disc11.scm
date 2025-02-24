;; Q1: Mystery Macro
;; Answer: This macro is used to substitute oprator and oprands in an expression `expr`,
;;      which are equal to `old`, with `new`, so that a new expression is built and evaluated.
;; e.g.
;; > (mystery-macro (+ 1 1) 1 2)        ;; -> (+ 2 2)
;; 4 
;; > (mystery-macro (+ 3 4) + *)        ;; -> (* 3 4)
;; 12

;; Q2: Multiple Assignment
(define-macro (assign sym1 sym2 expr1 expr2)
  `(begin
     (define ,sym1 ,expr1)
     (define ,sym2 ,(if (symbol? (eval expr2)) `(quote ,(eval expr2)) (eval expr2)))
   )
)

(assign x y (+ 1 1) 3)
(assign x y y x)
(expect x 3)
(expect y 2)

(define z 'x)      ; z is bound to the symbol x
(assign v w 2 z)   ; now v is bound to 2 and w is bound to the symbol x
(assign v w w v)   ; swap the values of v and w
(expect v x)
(expect w 2)

;; Q3: Switch
(define-macro (switch expr cases)
    `(let ((val ,expr))
	    ,(cons
                'cond
                (map 
                    (lambda (case) (cons `(equal? val ,(car case)) (cdr case)))
                    cases
                )
            )
    )
)

(define m
    (switch (+ 1 1) 
        (
            (1 'a)
            (2 'b)
            (3 'c)
        )
    )
)
(expect m b)
