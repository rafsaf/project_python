import tkinter as tk
import matplotlib.pyplot as plt

root = tk.Tk()
S = tk.Scrollbar(root)
T = tk.Text(root, height=60, width=120)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(tk.END, quote)
tk.mainloop()
x = [2000]
y = [35000]
z = [-40000]
c = [-18900]
k = [40000]
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
aaa = [2000,35000,40000,0,0]
bbb = [0,0,0,-40000,-18900]

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        if height != 0:
            axes[0][0].annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
f, axes = plt.subplots(2, 2)


x1 = axes[0][0].bar([0.5,1,1.5,2,2.5], bbb, 0.4, color='red', label='Zyski')
x2 = axes[0][0].bar([0.5,1,1.5,2,2.5], aaa, 0.4, color='blue', label='Koszty')
axes[0][0].set_xticks([0.5,1,1.5,2,2.5])
axes[0][0].set_xticklabels(labels)
autolabel(x1)
autolabel(x2)



axes[0][1].plot(x, y)
axes[1][0].plot(x, y)
axes[1][1].plot(x, y)

plt.show()
