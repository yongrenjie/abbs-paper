import penguins as pg
import aptenodytes as apt
import matplotlib.pyplot as plt

apt.thesis()
plt.rcParams['font.size'] = 8

p = apt.nmrd() / '221209-7c-abbs'
dss = pg.read(p, range(2001, 2004))

fig, axs = apt.subplots_2d_21(width=4.5, height=4.5)

h1_bounds1 = (0.5, 3.2)
h1_bounds2 = (0.5, 6.3)
c13_bounds = (15, 60)
n15_bounds = (110, 130)

dss[0].stage(ax=axs[0], levels=3.5e4, f1_bounds=c13_bounds, f2_bounds=h1_bounds1)
dss[1].stage(ax=axs[1], levels=3.5e4, f1_bounds=n15_bounds, f2_bounds=h1_bounds2)
dss[2].stage(ax=axs[2], levels=3.5e4, f1_bounds=n15_bounds, f2_bounds=h1_bounds2)


titles = [
    # f'1,1-ADEQUATE (TD1 = {dss[0]["td"][0]:.0f})',
    # f'$^{{15}}$N HMBC ({dss[1]["cnst23"]:.0f} Hz, TD1 = {dss[1]["td"][0]:.0f})',
    # f'$^{{15}}$N HMBC ({dss[2]["cnst24"]:.0f} Hz, TD1 = {dss[2]["td"][0]:.0f})',
    f'1,1-ADEQUATE',
    f'$^{{15}}$N HMBC ({dss[1]["cnst23"]:.0f} Hz)',
    f'$^{{15}}$N HMBC ({dss[2]["cnst24"]:.0f} Hz)',
]

pg.mkplots(axs, titles=titles)
pg.ymove(axs)
apt.label_axes_def(axs, fontsize=8)
# apt.show()
apt.save(__file__)
