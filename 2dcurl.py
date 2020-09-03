from manimlib.imports import *
import math

def functioncurlreal(p, velocity=0.1):
    x, y = p[:2]
    result =  (y**3-9*y) * RIGHT + (x**3-9*x) * UP
    result *= velocity
    return result

class curlScene(Scene):
    def construct(self):
        axes = Axes(
                number_line_config={
                "color": "#66FFFF",
                "stroke_width": 10,
                "include_tip": False,
                "tick_size": 0.01,
            },
                    
                    x_axis_config={
                "unit_size": 1,
                "tick_frequency": 0.5,
                
            },
            y_axis_config={
                "unit_size": 1,
                "tick_frequency": 0.5,
                
            },)
        self.add(axes)
        
        
        
        vector_field = VectorField(functioncurlreal, color=YELLOW)
        dots=[]
        numpts=50
        for i in range(numpts):
            for j in range(numpts):
               dots.append(SmallDot([i/2-numpts/4,j/2-numpts/4,0], color=BLUE)) 
        ##self.add(vector_field)
        ## self.wait(4)
        for i in range(numpts**2):
             self.add(dots[i])
        self.wait()
        for dot in dots:
            move_submobjects_along_vector_field(
                dot,
                lambda p: functioncurlreal(p,0.1) #0.5
            )
        self.add(vector_field)
        self.wait(4)
        self.wait(30)
        for dot in dots:
            dot.clear_updaters()
        self.wait()