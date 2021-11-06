import pathlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

log_file = pathlib.Path(__file__).resolve().parent / "public" / "touch.log"

with open(log_file) as f:
    logs = f.readlines()


is_touch = False

xs, ys = [], []
fig, ax = plt.subplots()
ax.invert_yaxis()
ax.set_xticks(np.arange(0, 101), minor=True)
ax.set_yticks(np.arange(0, 101), minor=True)
ax.grid(which="major", alpha=0.6)
ax.grid(which="minor", alpha=0.3)


for log in logs:

    log = log.replace("/ ", "/")
    if "TOUCH_DOWN" in log and log.split()[3] == '0':
        is_touch = True
        prev_x, prev_y = map(float, log.split()[5].split("/"))
        # xs.append(prev_x)
        # ys.append(prev_y)

    if "TOUCH_MOTION" in log and log.split()[3] == '0' and is_touch:
        x, y = map(float, log.split()[5].split("/"))

        # ax.plot([prev_x, x], [prev_y, y])

        prev_x, prev_y = x, y
        # xs.append(prev_x)
        # ys.append(prev_y)

    if "TOUCH_UP" in log:
        is_touch = False
        xs.append(prev_x)
        ys.append(prev_y)


def find_key(x, y):
    min_dist = 10000000
    key_pos = {
        "q": (23, 73), "w": (28, 73), "e": (33, 73), "r": (38, 73), "t": (43, 73), "y": (48, 73), "u": (54, 73), "i": (59, 73), "o": (63, 73), "p": (69, 73), "[back]": (76, 73),
        "a": (26, 81), "s": (31, 81), "d": (36, 81), "f": (41, 81), "g": (46, 81), "h": (51, 81), "j": (56, 81), "k": (61, 81), "l": (66, 81), "\n": (74, 81),
        "\\": (24, 90), "z": (31, 90), "x": (36, 90), "c": (41, 90), "v": (46, 90), "b": (51, 90), "n": (56, 90), "m": (61, 90),
        ".": (61, 95), "#": (23, 96)
    }

    for _key, pos in key_pos.items():
        dist = (pos[0] - x)*(pos[0] - x) + (pos[1] - y)*(pos[1] - y)
        if dist < min_dist:
            key = _key
            min_dist = dist

    return key


key_log = []

for i in range(len(xs)):
    x, y = xs[i], ys[i]
    if 34 <= x <= 55 and 93 <= y <= 100:
        key_log += " "
    elif 20 <= x <= 80 and 70 <= y:
        key = find_key(x, y)
        if key == "\b":
            key_log = key_log[:-1]
        else:
            key_log.append(key)

    if "".join(key_log[-11:]) == "fluxmanfred":
        pass_idx = i+1

print("".join(key_log))
ax.scatter(xs[:pass_idx], ys[:pass_idx], s=5)
ax.scatter(xs[pass_idx:], ys[pass_idx:], s=1)
plt.savefig("image.png")


fig_scatter = plt.figure()
plt_scatter = []

symbol_mode = False

# 実行
for i in range(len(xs) - pass_idx):

    x_scatter = plt.scatter(xs[:pass_idx+i], ys[:pass_idx+i], c="blue")

    if find_key(xs[pass_idx+i], ys[pass_idx+i]) == "#":
        symbol_mode = not symbol_mode

    if symbol_mode:
        x_scatter_red = plt.scatter(xs[pass_idx+i], ys[pass_idx+i], c="yellow")
    else:
        x_scatter_red = plt.scatter(xs[pass_idx+i], ys[pass_idx+i], c="red")

    plt_scatter.append([x_scatter, x_scatter_red])

plt.grid(True)

ani = animation.ArtistAnimation(fig_scatter, plt_scatter, interval=500)

# 保存
ani.save('sample.gif', writer="imagemagick")
