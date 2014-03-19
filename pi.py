import matplotlib.pyplot as plot
from numpy import sqrt 
from numpy import meshgrid
from numpy import arange

xs = arange(-3, 4, 0.01)
ys = arange(0, 6, 0.01)
x, y = meshgrid(xs, ys)
 
lline = 4.23*x*sqrt(abs((x+0.7439)*(x+1.094))/((-0.7439-x)*(x+1.094))) - 0.35*y + 5.05
rline = 4.16*x*sqrt(abs((x-1.22)*(x-1.49))/((1.22-x)*(x-1.49))) + 0.25*y - 6.45
bar = y - 5.438*sqrt(abs((x+1.47)*(x-3.28))/((3.28-x)*(1.47+x)))
head = (((x+1.49)**2)/1.25)*sqrt(abs((x+2.48)*(x+1.47))/(-(x+2.48)*(x+1.47))) + (((y-3.36)**2)/4.27)*sqrt(abs((y-4.3)*(y-5.438))/((y-4.3)*(5.438-y))) - 1
rstem = (((x-2.25)**2)/1.14)*sqrt(abs((x-1.49)*(x-3.28))/((3.28-x)*(x-1.49))) + (((y-2.16)**2)/2.8)*sqrt(abs((y-1.69))/(1.69-y)) - 1
lstem = (((x+1.72)**2)/0.53)*sqrt(abs((x+1.49)*(x+1.094))/((x+1.49)*(-1.094-x))) + (((y-2.01)**2)/2.56)*sqrt(abs((y-0.49)*(y-1.1935))/((y-0.49)*(1.1935-y))) -1
 
for f in [lline, rline, bar, head, rstem, lstem]:
    plot.contour(x, y, f, [0])
	
#plot.grid() 
plot.show()
