import matplotlib.pyplot as plt
from matplotlib.path import Path

def IsPointInPolygon(point):
     path = Path(cords2)
     for point in points:
      if path.contains_point(point):
        print(f"Точка {point} лежит внутри полигона")
      else:
        print(f"Точка {point} лежит снаружи полигона")
    
cords2 = [(2, 1), (4, 7), (8, 0), (4, -5)]
points = [(4, 1)]

IsPointInPolygon(points)
cords2.append(cords2[0])
xs, ys = zip(*cords2)
plt.figure()
plt.plot(xs, ys)
xs, ys = zip(*points)
plt.scatter(xs, ys, color="red") 
plt.grid()
plt.show()
plt.show()