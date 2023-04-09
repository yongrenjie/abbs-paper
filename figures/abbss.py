import penguins as pg
import aptenodytes as apt
import matplotlib.pyplot as plt

apt.thesis()
plt.rcParams['font.size'] = 8

p = apt.nmrd() / '220722-7c-abbs'
dss = pg.read(p, range(14001, 14006))

fig, axs = apt.subplots_2d_32(width=6.5, height=4.5)

h1_bounds1 = (0.5, 6.1)
h1_bounds2 = (0.5, 8.5)
h1_bounds3 = (7.2, 8.5)
c13_bounds1 = (6, 178)
c13_bounds2 = (6, 135)
n15_bounds1 = (110, 130)
n15_bounds2 = (114, 130)

dss[0].stage(ax=axs[0], levels=4.5e4, f1_bounds=c13_bounds1, f2_bounds=h1_bounds1)
dss[1].stage(ax=axs[1], levels=1.8e4, f1_bounds=n15_bounds1, f2_bounds=h1_bounds1)
dss[2].stage(ax=axs[2], levels=2.5e5, f1_bounds=c13_bounds1, f2_bounds=h1_bounds2)
dss[3].stage(ax=axs[3], levels=2.5e5, f1_bounds=n15_bounds2, f2_bounds=h1_bounds3)
dss[4].stage(ax=axs[4], levels=2.5e5, f1_bounds=c13_bounds2, f2_bounds=h1_bounds1)

titles = [
    f'1,1-ADEQUATE',
    f'$^{{15}}$N HMBC',
    f'$^{{13}}$C HMBC',
    f'$^{{15}}$N seHSQC',
    f'$^{{13}}$C HSQC',
    # f'1,1-ADEQUATE (NS = {dss[0]["ns"]:.0f})',
    # f'$^{{15}}$N HMBC ({dss[1]["cnst23"]:.0f} Hz, NS = {dss[1]["ns"]:.0f})',
    # f'$^{{13}}$C HMBC ({dss[2]["cnst13"]:.0f} Hz, NS = {dss[2]["ns"]:.0f})',
    # f'$^{{15}}$N seHSQC (NS = {dss[3]["ns"]:.0f})',
    # f'$^{{13}}$C HSQC (NS = {dss[4]["ns"]:.0f})',
]

pg.mkplots(axs, titles=titles)
pg.ymove(axs)

apt.label_axes_def(axs, fontsize=8)
# apt.show()
apt.save(__file__)
