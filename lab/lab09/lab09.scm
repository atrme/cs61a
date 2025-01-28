(define (over-or-under num1 num2) 
    (cond
        ((= num1 num2) 0)
        ((> num1 num2) 1)
        ((< num1 num2) -1)
    )
)
(define (over-or-under-ifversion num1 num2) 
    (if (= num1 num2)
        0
        (if (> num1 num2) 
             1 
            -1
        ) 
    )
)

(define (make-adder num) 
    (define (adder inc)
        (+ num inc) 
    )
    adder
)

(define (composed f g) 
    ( lambda (x) (f (g x)) )
)

(define (repeat f n) 
    (define (repeated remain x)
        (if (= remain 0)
            x
            (repeated (- remain 1) (f x))
        )
    )
    (lambda (x) (repeated n x))
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
    (define big (max a b))
    (define small (min a b))
    (if (zero? (modulo big small))
        small
        (gcd small (modulo big small))
    )
)
