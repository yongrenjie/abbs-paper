import penguins as pg
import aptenodytes as apt

apt.fira()

p = apt.nmrd() / '220604-7x-abbs'
dss = pg.read(p, range(111001, 111005))

k = 0.8
fig, axs = pg.subplots2d(2, 2, figsize=(8*k, 8*k))

h1_bounds1 = (1, 8.2)
h1_bounds2 = (1, 4.2)
h1_bounds3 = (1, 4.7)
c13_bounds1 = (20, 175)
c13_bounds2 = (20, 135)
n15_bounds = (20, 160)

dss[0].stage(ax=axs[0][0], levels=1e3, f1_bounds=c13_bounds1, f2_bounds=h1_bounds1)
dss[1].stage(ax=axs[0][1], levels=7e2, f1_bounds=n15_bounds, f2_bounds=h1_bounds2)
dss[2].stage(ax=axs[1][0], levels=9e4, f1_bounds=h1_bounds3, f2_bounds=h1_bounds3)
dss[3].stage(ax=axs[1][1], levels=1.2e4, f1_bounds=c13_bounds2, f2_bounds=h1_bounds1)


titles = [
    f'1,1-ADEQUATE',
    f'$^{{15}}$N HMBC',
    f'NOESY',
    f'$^{{13}}$C HSQC',
    # f'1,1-ADEQUATE (NS = {dss[0]["ns"]:.0f})',
    # f'$^{{15}}$N HMBC ({dss[1]["cnst23"]:.0f} Hz, NS = {dss[1]["ns"]:.0f})',
    # f'$^{{13}}$C HMBC ({dss[2]["cnst13"]:.0f} Hz, NS = {dss[2]["ns"]:.0f})',
    # f'$^{{13}}$C HSQC (NS = {dss[3]["ns"]:.0f})',
]

pg.mkplots(axs, titles=titles)
pg.ymove(axs)

apt.label_axes_def(axs)
# apt.show()
apt.save(__file__)
