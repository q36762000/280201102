import math
class Cylinder:
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height
  
  def get_radius(self):
    return self.radius
  
  def set_radius(self, radius):
    if radius > 0:
      self.radius = radius
  
  def get_height(self):
    return self.radius
  
  def set_height(self, height):
    if height > 0:
      self.radius = height
  
  def base_area(self):
    return math.pi*(self.radius**2)
  
  def surface_area(self):
    return 2*math.pi*self.radius*self.height
  
  def area(self):
    return 2*(self.base_area()+self.surface_area())
  
  def volume(self):
    return self.base_area()*self.height()

c1 = Cylinder(radius=3,height=5)
c1.set_height(5)
print(c1.base_area())