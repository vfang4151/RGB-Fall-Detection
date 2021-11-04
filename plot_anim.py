import sys
import json

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

if len(sys.argv) < 2:
    print('*E* -- Please provide a file.') 

file = sys.argv[1];
f = open(file)
Lines = f.readlines();

mid_list = [[1,2],[5,6],[11,12]]
left_list = [[0,1],[1,3],[3,5],[5,7],[7,9],[5,11],[11,13],[13,15]]
right_list = [[0,2],[2,4],[4,6],[6,8],[8,10],[6,12],[12,14],[14,16]]
bone_list = mid_list+left_list+right_list

count = 0
xary = []
yary = []
# Strips the newline character
for line in Lines:
    count += 1
#    print(count)
    data = json.loads(line)
    d1 = data["predictions"]
    xdata = []
    ydata = []
#    print(len(d1))
    for ind in range(len(d1)):
        bbox = d1[ind]['bbox']
        if bbox[0] < 320:
            continue
#        print("count =", count, "ind =",ind)
#        print(bbox)
        if (file.find("fall-13") == 0 or file.find("fall-14") == 0) and bbox[0] < 370: # labeling mutiple persons
            continue
        keys = d1[ind]['keypoints']
        x = []
        y = []
        for i in range(17):
            x.append(keys[i*3]-320)
            y.append(239-keys[i*3+1])
        for bone in bone_list:
            if (x[bone[0]] < 320) and (x[bone[0]] > 0) and (x[bone[1]] > 0) and (x[bone[1]] < 320):
                xdata.append([x[bone[0]], x[bone[1]]])
                ydata.append([y[bone[0]], y[bone[1]]])
    xary.append(xdata)
    yary.append(ydata)
print(len(xary))

xx = []
yy = []

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

fig, ax = plt.subplots()
ax.set_xlim(0,320)
ax.set_ylim(0,240)

def animate(i):
    ax.clear()
    ax.set_xlim(0,320)
    ax.set_ylim(0,240)
    ax.grid(True)
    xx = xary[i]
    yy = yary[i]
    #print("---",i,"---")
    for j in range(len(xx)):
        ax.plot(xx[j],yy[j],'b')
        #print(xx[j], ",", yy[j])
    ax.scatter(xx,yy,s=15)
   
anim = FuncAnimation(fig, animate, frames=len(xary), interval=1, repeat=False)
#anim.save('ani.mp4', writer=writer)

plt.grid(True)
plt.show()

#plt.close("all")


