import seagull as sg
from seagull import lifeforms as lf
import matplotlib.pyplot as plt

LOOP_LENGHT = 600
#You can fix this bug also by changing the variable name to LOOP_LENGTH 
plt.rcParams["animation.html"] = 'jshtml'

#I see another bug also in the code, the variable name is LOOP_LENGHT, but it should be LOOP_LENGTH
board = sg.Board(size=(30,30))
board.add(lf.Blinker(length=3), loc=(4,4))
board.add(lf.Glider(), loc=(10,4))
board.add(lf.Glider(), loc=(15,4))
board.add(lf.Pulsar(), loc=(5,12))
#board.view()

sim = sg.Simulator(board)
hist = sim.run(sg.rules.conway_classic, iters=LOOP_LENGHT)
sim.animate(interval= LOOP_LENGHT / 10)