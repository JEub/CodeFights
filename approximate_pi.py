import random

## Given a square with length = width = L,
## Embed a circle with radius = 1/2*L so that circle is centered at center of square.

def add_point(L):
    """
    Add a random point to the frame.
    """
    # center of object
    x,y = 0,0
    
    random_x = x + L/2 * (-1+2*random.random())
    random_y = x + L/2 * (-1+2*random.random())
    
    return (random_x, random_y)
    
def inside_circle(x,y,L):
    distance_from_center = (x**2 + y**2)
    
    if distance_from_center < L/2:
        return True
    else:
        return False
        
## Simulate Large number of points and calculate pi
def compute_simulation_pi(n, L=2):
    
    points_in_circle = 0
    for i in range(n):
        r1,r2 = add_point(L)
        if inside_circle(r1,r2,L):
            points_in_circle += 1
        
    result = 4*(points_in_circle/n)
    
    return result
