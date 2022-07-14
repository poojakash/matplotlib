import matplotlib.pyplot as pt

x=[]
y=[]
f=open('coordinates.txt','r')
data=f.read().splitlines()

for i in data:
    z=i.split(',')
    x.append(int(z[0]))
    y.append(int(z[1]))
pt.plot(x,y)
pt.show()