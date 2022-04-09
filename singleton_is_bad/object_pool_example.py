
class Reusable:
    def test(self):
        print(f"using object {id(self)}")


class ReusablePool:
    def __init__(self, size) -> None:
        self.size = size
        self.free = []
        self.in_use = []
    
        for _ in range(size):
            self.free.append(Reusable())
    
    def acquire(self) -> Reusable:
        if len(self.free) <= 0:
            raise Exception("no more objects...")
        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r
    
    def release(self, r: Reusable):
        self.in_use.remove(r)
        self.free.append(r)

p = ReusablePool(2)

r = p.acquire()
r.test()

r2 = p.acquire()
r2.test()

p.release(r2)

r3 = p.acquire()
r3.test()  # same as r2, they are same object!!