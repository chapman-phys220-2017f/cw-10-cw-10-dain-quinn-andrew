#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML

"""2D Random walk library

This module introduces Monte Carlo techniques by showing how to simulate
many particles that randomly walk around a 2D lattice. This is a crude but
effective model for heat transfer, as well as air diffusion.
"""

def walk_gen(walkers=10, steps_per_frame=1):
    """Generator for 2D random walkers
    Yields x and y coordinate arrays for particles that randomly walk around
    a 2D lattice indexed by integers. Each walker may move in one of four
    cardinal directions randomly, on each time step. The generator yields all
    new positions with each iteration.
    
    Args:
      walkers : int, number of walkers
      steps_per_frame : number of internal steps to take before each yield
    
    Returns:
      (xs, ys) : tuple of arrays of x and y coordinate integers for all walkers
    """
    xs = np.zeros(walkers)
    ys = np.zeros(walkers)
    EAST, WEST, NORTH, SOUTH = 0, 1, 2, 3 
    while True:
        for step in range(steps_per_frame):
            moves = np.random.randint(4, size=walkers)
            xs += np.where(moves == EAST, 1, 0)
            xs -= np.where(moves == WEST, 1, 0)
            ys += np.where(moves == NORTH, 1, 0)
            ys -= np.where(moves == SOUTH, 1, 0)
        yield (xs,ys)
        
def walk_gen1(walkers=10, steps_per_frame=1):
    """Generator for 2D random walkers
    Yields x and y coordinate arrays for particles that randomly walk around
    a 2D lattice indexed by integers. Each walker may move in one of four
    cardinal directions randomly, on each time step. The generator yields all
    new positions with each iteration.
    
    Args:
      walkers : int, number of walkers
      steps_per_frame : number of internal steps to take before each yield
    
    Returns:
      (xs, ys) : tuple of arrays of x and y coordinate integers for all walkers
    """
    forbidL = []
    forbidT = []
    forbidB = []
    forbidR = []
    for in in range(-19,20):
        forbidL.append((19,i))
    for i in range(-19,20):
        forbidT.append((i,19))
        forbidB.append((i,-19))
    for i in range(5,19):
        forbidR.append((19,i))
        forbidR.append((19,-i))
    xs = np.zeros(walkers)
    ys = np.zeros(walkers)
    EAST, WEST, NORTH, SOUTH = 0, 1, 2, 3 
    while True:
        for step in range(steps_per_frame):
            if (xs,ys) 
            else:
                moves = np.random.randint(4, size=walkers)
                xs += np.where(moves == EAST, 1, 0)
                xs -= np.where(moves == WEST, 1, 0)
                ys += np.where(moves == NORTH, 1, 0)
                ys -= np.where(moves == SOUTH, 1, 0)
        yield (xs,ys)

def plot_anim(frame_gen, xlim=(-30,30), ylim=(-30,30), delay=20, max_frames=100,
                   title=None, xlabel=None, ylabel=None, gif=False):
    """Produce a scatterplot point animation from a frame-generating function. 
    Works in two modes:
      - Return a Jupyter HTML5 wrapper around a rendered mp4 video of the animation
      - Create an animated gif file of the animation
    The first mode is default and recommended for in-notebook rendering.
    
    Args:
      frame_gen : Generator that yields successive tuples (xs, ys) of 
                  points, as domain and range arrays, to plot as frames.
                  The frames will continue until max_frames is reached.
      xlim = (xmin,xmax) : Horizontal plot range 
      ylim = (ymin,ymax) : Vertical plot range  
      delay : number of ms between frames
      max_frames : maximum number of saved frame 
      title : plot title (optional)
      xlabel : plot x axis label (optional)
      ylabel : plot y axis label (optional)
      gif : Boolean, if true render gif file instead of outputting HTML5 
    
    Returns:
      HTML object containing mp4 video of animation (when gif false)
    
    Effects:
      Saves a gif file containing the animation (when gif true)
    """
    # Create empty plot set to desired fixed zoom
    fig, ax = plt.subplots()
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    if title:  plt.title(title)
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    
    # Draw an empty line and save the handle to update later
    line, = ax.plot([], [], 'r.', alpha=0.4)
    
    # Define how to generate a blank frame
    def init_frame():
        line.set_data([],[])
        return (line,)
    
    # Define how to update a frame 
    def animate(i):
        x,y = next(frame_gen)
        line.set_data(x,y)
        return (line,)
    
    # Define animation object using frame generator
    # Use blit to redraw only the changes that were made
    anim = animation.FuncAnimation(fig, animate, init_func=init_frame, 
                                   frames=range(max_frames), interval=delay, 
                                   save_count=max_frames, blit=True)
    
    # Tidy up stray plot within the notebook itself
    plt.close()
    
    if gif:
        # Render animation as animated gif file
        anim.save(frame_gen.__name__+'.gif', writer='imagemagick')
    else:
        # Make sure that animation renders to HTML5 by default
        rc('animation', html='html5')
        # Convert animation to HTML5 and return
        return HTML(anim.to_html5_video())
