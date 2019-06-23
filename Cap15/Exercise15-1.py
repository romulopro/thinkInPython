'''
Created on 6 de nov de 2018

@author: Romulo
'''
import math, turtle
class Circle():
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        
    def point_in_circle(self, point_x, point_y):
        dist_of_point_to_center = math.sqrt((point_x - self.center_x)**2 + (point_y - self.center_y)**2)
        if (self.radius >= dist_of_point_to_center): 
            return True
        return False
    
    def rect_in_circle(self, point_x_sup, point_y_sup, point_x_inf, point_y_inf):
        if self.point_in_circle(point_x_sup, point_y_sup) is False:
            return False
        if self.point_in_circle(point_x_sup, point_y_inf) is False:
            return False
        if self.point_in_circle(point_x_inf, point_y_inf) is False:
            return False
        if self.point_in_circle(point_x_inf, point_y_sup) is False:
            return False
        return True
    
    def  rect_circle_overlap(self, point_x_sup, point_y_sup, point_x_inf, point_y_inf):
        if self.point_in_circle(point_x_sup, point_y_sup):
            return True
        if self.point_in_circle(point_x_sup, point_y_inf):
            return True
        if self.point_in_circle(point_x_inf, point_y_inf):
            return True
        if self.point_in_circle(point_x_inf, point_y_sup):
            return True
        return False
    
    def draw_circle(self):
        pencil = turtle.Turtle()
        pencil.penup()
        pencil.goto(self.center_x, self.center_y - self.radius)
        pencil.pendown()
        pencil.circle(self.radius)
        pencil.hideturtle() 
        return
    
    def draw_rect(self, point_x_sup, point_y_sup, point_x_inf, point_y_inf):
        pencil_rect = turtle.Turtle()
        pencil_rect.penup()
        pencil_rect.goto(point_x_sup, point_y_sup)
        pencil_rect.pendown()
        pencil_rect.goto(point_x_sup, point_y_inf)
        pencil_rect.goto(point_x_inf, point_y_inf)
        pencil_rect.goto(point_x_inf, point_y_sup)
        pencil_rect.goto(point_x_sup, point_y_sup)
        
        return
        

        
    
if __name__ == '__main__':
    c1 = Circle(150,100,50)
    print("Is the point inside the circle? " , c1.point_in_circle(77, 77.01))
    print("Is the rectangle inside the circle? " , c1.rect_in_circle(150, 100, 60, 20))
    print("Is at least one corner of rectangle inside the circle? " , c1.rect_circle_overlap(70, 100, 60, 20))
    c1.draw_circle()
    c1.draw_rect(70, 100, 60, 20)
    turtle.Screen().mainloop()
    
    
    