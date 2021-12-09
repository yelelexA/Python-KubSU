import math

class Triangle(object):

    _coordinates = []

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self._coordinates = [x1, y1, x2, y2, x3, y3]

    def getCoordinats(self):
        return self._coordinates

    def get_sides(self):
        sides = []
        for i in range(0,len(self._coordinates)-3,2):
            sides.append(self._side(self._coordinates[i],self._coordinates[i+1],self._coordinates[i+2],self._coordinates[i+3]))
        sides.append(self._side(self._coordinates[0],self._coordinates[1],self._coordinates[-2],self._coordinates[-1]))

        return sides

    def perimetr(self):
        p = 0
        for i in self.get_sides():
            p += i
        return p

    def _side(self, l1, k1, l2, k2):
      try:
        return math.sqrt((l2 - l1) ** 2 + (k2 - k1) ** 2)
      except Exception:
        print("Ошибка при вычислении стороны!!!")
        self._coordinates = None
        sides = None

    def square(self):
     return 0.5 * math.fabs((self._coordinates[0] - self._coordinates[4]) * (self._coordinates[3] - self._coordinates[5]) - (self._coordinates[2] - self._coordinates[4]) * (self._coordinates[1] - self._coordinates[5]))

    def move(self, x_step, y_step):
       try:
          for i in range(len(self._coordinates)):
            if i % 2 == 0:
             self._coordinates[i] += x_step
            if i % 2 != 0:
             self._coordinates[i] += y_step

          return self._coordinates

       except Exception:
           return "Ошибка при перемещении объекта на плоскости!!!"

class Pentagon(Triangle):

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
        self._coordinates = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]

    def square(self):
        s = 0

        for i in range(0,len(self._coordinates)-3,2):
           s+=self._coordinates[i]*self._coordinates[i+3]
        s+=self._coordinates[-2]*self._coordinates[1]

        for j in range(1,len(self._coordinates)-1,2):
            s-=self._coordinates[j+1]*self._coordinates[j]
        s-=self._coordinates[0]*self._coordinates[-1]

        return 0.5*math.fabs(s)

def compare(t1,t2):
  try:
     s1 = t1.square()
     s2 = t2.square()
     if s1 > s2:
         print("1 объект больше по площади")
     elif s1 < s2:
         print("2 объект больше по площади")

     else: print("Объекты равны по площади")

  except Exception:
        print("Ошибка при сравнении площадей двух объектов!!!!")

try:
 #4,1,2,6,3,10
# 1,-1,-1,-1, 0, 2.08
#-4, -3, -1, 3, 5, 0
 tr = Triangle(1,-1,-1,-1, 0, 2.08)
 print("Координаты треугольника:", tr.getCoordinats())
 print("Длины сторон треугольника:", tr.get_sides())
 print("Измененные координаты:", tr.move(5,2))
 print("Площадь треугольника:", tr.square())

 # # 1,-1,-1,-1,-1.62, 0.9, 0, 2.08, 1.62,0.9
 #1,-1,-1,-1, -2,2, 1, 1,3, 0
 #-2, -1.5, -1, 0.5, -2, 2, 1.5, 1.5, 0.5, -0.5
 pn = Pentagon(1,-1,-1,-1, -2,2, 1, 1,3, 0)
 print("\nКоординаты пентагона:",pn.getCoordinats())
 print("Длины сторон пентагона:",pn.get_sides())
 print("Измененные координаты:",pn.move(3,1))
 print("Площадь пентагона",pn.square())

 print("\n")
 compare(tr,pn)

except Exception:
    print('\n\n| Перепроверьте указанные данные и попробуйте снова! |\n\n')

