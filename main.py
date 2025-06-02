from controller import * 

a1=Actor('Смит','Джон',10,1300)
a2=Actor('Кузнецов','Иван',22,900)
a3=Actor('Шмидт','Иоганн',13,1500)
a4=Actor('Ферреро','Джованни',32,1500)
a5=Actor('Макгоуэн','Шон',15,1000)
base=Base([a1,a2,a3,a4,a5], 12)
def start(b : Base):
    a=Win(b)

start(base)