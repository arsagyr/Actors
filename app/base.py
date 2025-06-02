class Base:
    def __init__(self, a , n = 12):
        self.a = a
        self.c=len(self.a)
        self.max = n
    def add(self, a):
        b = True
        if self.c<=12:
            self.a.append(a)
            self.c=self.c+1
        else:
            b = False
        return b
    def print(self):
        print(self.a)