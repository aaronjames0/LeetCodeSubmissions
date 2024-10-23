from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock() #create locks
        self.nonzero_lock = Lock()
        self.odd_lock = Lock()
        self.even_lock = Lock()
        self.nonzero_lock.acquire() # prevent the printing of a nonzero until nonzero_lock is released
        self.even_lock.acquire() # prevent the printing of an even until even_lock is released

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n): # iterate length of n
            self.zero_lock.acquire() # prevent next iteration until zero_lock is released
            printNumber(0)
            self.nonzero_lock.release() # allow the printing of the next nonzero 

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for num in range(2, self.n+1, 2): # iterate even numbers
            self.even_lock.acquire() # prevent next iteration until even_lock is released
            self.nonzero_lock.acquire() # prevent next nonzero until nonzero_lock is released
            printNumber(num)
            self.zero_lock.release() # allow the printing of the next zero
            self.odd_lock.release() # allow the printing of the next odd

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for num in range(1, self.n+1, 2): # iterate odd numbers
            self.odd_lock.acquire() # prevent next iteration until odd_lock is released
            self.nonzero_lock.acquire() # prevent next nonzero until nonzero_lock is released
            printNumber(num)
            self.zero_lock.release() # allow the printing of the next zero
            self.even_lock.release() # allow the printing of the next even