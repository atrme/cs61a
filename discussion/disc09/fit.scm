; Return whether there are n perfect squares with no repeats that sum to total

    (define (fit total n)
        (define (f total n k)
            (if (and (= n 0) (= total 0))
                #t
            (if (< total (* k k))
                #f
                (and 
                    (not (< n 0)) 
                    (or 
                        (f total n (+ k 1))
                        (f (- total (* k k)) (- n 1) (+ k 1))
                    ) 
            )))
        (f total n 1))

    (expect (fit 10 2) #t)  ; 1*1 + 3*3
    (expect (fit 9 1) #t)   ; 3*3
    (expect (fit 9 2) #f)   ;
    (expect (fit 9 3) #f)   ; 1*1 + 2*2 + 2*2 doesn't count because of repeated 2*2
    (expect (fit 25 1) #t)  ; 5*5
    (expect (fit 25 2) #t)  ; 3*3 + 4*4

;Equivalent python function acquiring the same effect

;def fit(total, n):
;   def f(total, n, k):
;        if (n == 0) and (total == 0):
;            return True
;        elif total < k*k:
;            return False
;        else:
;            return not (n < 0) and (f(total, n, k+1) or f(total-k*k, n-1, k+1))
;    return f(total, n, 1)
