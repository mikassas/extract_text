import numpy as np
import gizeh as gz
import moviepy.editor as mpy

w = h = 150
d = 2
nballs = 60

radii = np.random.randint(.1*w, .2*w, nballs)
collors = np.random.rand(nballs, 3)
centers = np.random.randint(0, w, (nballs, 2))


def make_frame(t):
    surface = gz.Surface(w,h)
    for r, color, center in zip(radii, collors, centers):
        angle = 2*np.pi*(t/d*np.sign(color[0]-.5)+color[1])
        xy = center+gz.polar2cart(w/5,angle) # center of the ball
        gradient = gz.ColorGradient(type="radial",
                    stops_colors = [(0,color),(1,color/10)],
                    xy1=[0.3,-0.3], xy2=[0,0], xy3 = [0,1.4])
        ball = gz.circle(r=1, fill=gradient).scale(r).translate(xy)
        ball.draw(surface)
    return surface.get_npimage()
    

if __name__ == "__main__":
    clip = mpy.VideoClip(make_frame, duration=d)
    clip.write_gif('balls.gif', fps=15, opt='OptimizePlus', fuzz=10)
