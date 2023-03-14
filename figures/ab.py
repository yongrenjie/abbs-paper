import penguins as pg
import aptenodytes as apt
import matplotlib.pyplot as plt

apt.thesis()
plt.rcParams['font.size'] = 8

p = apt.nmrd() / '220604-7x-abbs'
dss = pg.read(p, [23001, 23002])

fig, axs = pg.subplots2d(1, 2, figsize=(4.4, 2.3))

h1_bounds1 = (1, 8.2)
h1_bounds2 = (1, 4.2)
c13_bounds = (20, 175)
n15_bounds = (20, 160)

dss[0].stage(ax=axs[0], levels=8e4, f1_bounds=c13_bounds, f2_bounds=h1_bounds1)
dss[1].stage(ax=axs[1], levels=7e4, f1_bounds=n15_bounds, f2_bounds=h1_bounds2)

titles = [
    f'1,1-ADEQUATE',
    f'$^{{15}}$N HMBC',
]

pg.mkplots(axs, titles)
pg.ymove(axs)

apt.label_axes_def(axs, fontsize=8)
# apt.show()
apt.save(__file__)
