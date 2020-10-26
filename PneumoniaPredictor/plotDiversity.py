import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import matplotlib.patches as mpatches
import re


xlab = ['< .85', '.85-.9', '.9-.95', '>.95']
ylab = ["27.2(15.8)",  "47.3(17.1)", "61.5(5.3)", "71(2.8)"]
x = [1,2,3,4]
y = [1.8, 1.3, 1.25,  1.9]
sizes = [63, 100, 150,  230]
colors = ['C3'] * len(y)

fig, ax = plt.subplots(figsize=(8, 4))
scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.6, label="Mortality")

handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)


legend1 = ax.legend(handles, ylab, loc="lower right", title="Mean Age")
ax.add_artist(legend1)

prauc_patch = mpatches.Patch(color='C0', label='ROC-AUC')
prauc_patch.set_alpha(0.5)

plt.title('Mortality in Pneumonia Patients')
plt.xlabel('PR-AUC')
plt.ylabel("Average # of Pre-existing Conditions")
xticks = list(set(x))
plt.xticks(ticks=xticks, labels=xlab)

plt.savefig( "PMheterogeneity.pdf", bbox_inches='tight')

################ITU PNEUMONIA

xlab = ['< .85', '.85-.9', '.9-.95', '>.95']
ylab = ["38(11.2)", "53(14.6)", "61(13.4)", "69(14.6)"]
x = [1,2,3,4]
y = [1.59,  1.55, 1.47, 2.2]
sizes = [51, 100, 180, 250]
colors = ['C1'] * len(y)

fig, ax = plt.subplots(figsize=(8, 4))
scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.5, label="Mortality")

handles, labels = scatter.legend_elements(prop="sizes", alpha=0.5)


legend1 = ax.legend(handles, ylab, loc="lower right", title="Mean Age")
ax.add_artist(legend1)

prauc_patch = mpatches.Patch(color='C1', label='ROC-AUC')
prauc_patch.set_alpha(0.5)

plt.title('ITU Re-admission in Pneumonia Patients')
plt.xlabel('PR-AUC')
plt.ylabel("Average # of Pre-existing Conditions")
xticks = list(set(x))
plt.xticks(ticks=xticks, labels=xlab)

plt.savefig( "PIheterogeneity.pdf", bbox_inches='tight')



############## MORTALITY COVID

xlab = ['< .925', '.925-.95', '.96-.975', '>.975']
ylab = ["53(13.4)" , "61(12.3)", "69(13.7)", "69(9.6)"]
x = [1,2,3,4]
y = [1.8, 1.3, 1.6,  1.8]
sizes = [190,50, 130,  200]
colors = ['C3'] * len(y)

fig, ax = plt.subplots(figsize=(8, 4))
scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.5, label="Mortality")
ax.set_ylim(0,2.3)

handles, labels = scatter.legend_elements(prop="sizes", alpha=0.5)


legend1 = ax.legend(handles, ylab, loc="lower right", title="Mean Age")
ax.add_artist(legend1)

prauc_patch = mpatches.Patch(color='C0', label='ROC-AUC')
prauc_patch.set_alpha(0.5)

plt.title('Mortality in COVID-19 Patients')
plt.xlabel('PR-AUC')
plt.ylabel("Average # of Pre-existing Conditions")
xticks = list(set(x))
plt.xticks(ticks=xticks, labels=xlab)

plt.savefig( "CMheterogeneity.pdf", bbox_inches='tight')

###################################ITU COVID

xlab = ['< .925', '.925-.95', '.96-.975', '>.975']
ylab = ["53(8.4)"  , "61(7.3)","69(5.7)",  "69(9.6)"]

x = [1,2,3,4]
y = [1.6, 1.5, 1.4,  1.7]
sizes = [50, 100, 180,  185]
colors = ['C1'] * len(y)
fig, ax = plt.subplots(figsize=(8, 4))
scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.5, label="Mortality")
ax.set_ylim(0,2.3)

handles, labels = scatter.legend_elements(prop="sizes", alpha=0.5)


legend1 = ax.legend(handles, ylab, loc="lower right", title="Mean Age")
ax.add_artist(legend1)

prauc_patch = mpatches.Patch(color='C0', label='ROC-AUC')
prauc_patch.set_alpha(0.5)

plt.title('ITU Admission in COVID-19 Patients')
plt.xlabel('PR-AUC')
plt.ylabel("Average # of Pre-existing Conditions")
xticks = list(set(x))
plt.xticks(ticks=xticks, labels=xlab)

plt.savefig( "CIheterogeneity.pdf", bbox_inches='tight')



