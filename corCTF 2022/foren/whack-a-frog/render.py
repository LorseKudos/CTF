import pathlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
log_file = "move.txt"

with open(log_file) as f:
    logs = f.readlines()


is_drugging = True

xs, ys = [], []
fig, ax = plt.subplots()
ax.invert_yaxis()
# ax.set_xticks(np.arange(0, 101), minor=True)
# ax.set_yticks(np.arange(0, 101), minor=True)
# ax.grid(which="major", alpha=0.6)
# ax.grid(which="minor", alpha=0.3)

cnt = 1
for log in logs:

    log = log.split()
    if "mousedown" in log[2]:
        is_drugging = True
        prev_x, prev_y = int(log[0]), int(log[1])
        xs.append(prev_x)
        ys.append(prev_y)

    if "mousemove" in log[2] and is_drugging:
        x, y = int(log[0]), int(log[1])

        # ax.plot([prev_x, x], [prev_y, y])

        prev_x, prev_y = x, y
        xs.append(prev_x)
        ys.append(prev_y)

    if "mouseup" in log:
        is_drugging = False
        xs.append(prev_x)
        ys.append(prev_y)

        ax.scatter(xs, ys, s=1)
        plt.savefig(f"image{cnt}.png")
        cnt += 1
