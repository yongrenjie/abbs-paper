import penguins as pg
from aptenodytes import nmrd, fira

fira()

p = nmrd() / '220604-7x-abbs'
d = pg.read(p, 102)
dss = pg.read(p, range(102001, 102005))

k = 0.8
fig, axs = pg.subplots2d(2, 2, figsize=(8*k, 8*k))

h1_bounds1 = (1, 8.2)
h1_bounds2 = (1, 4.2)
c13_bounds1 = (20, 175)
c13_bounds2 = (20, 135)
n15_bounds = (20, 160)

dss[0].stage(ax=axs[0][0], levels=6e4, f1_bounds=c13_bounds1, f2_bounds=h1_bounds1)
dss[1].stage(ax=axs[0][1], levels=3.6e4, f1_bounds=n15_bounds, f2_bounds=h1_bounds2)
dss[2].stage(ax=axs[1][0], levels=1.7e5, f1_bounds=c13_bounds1, f2_bounds=h1_bounds1)
dss[3].stage(ax=axs[1][1], levels=2.5e5, f1_bounds=c13_bounds2, f2_bounds=h1_bounds1)


titles = [
    f'1,1-ADEQUATE (NS = {dss[0]["ns"]:.0f})',
    f'$^{{15}}$N HMBC ({dss[1]["cnst23"]:.0f} Hz, NS = {dss[1]["ns"]:.0f})',
    f'$^{{13}}$C HMBC ({dss[2]["cnst13"]:.0f} Hz, NS = {dss[2]["ns"]:.0f})',
    f'$^{{13}}$C HSQC (NS = {dss[3]["ns"]:.0f})',
]

pg.mkplots(axs, titles=titles)
pg.ymove(axs)
pg.label_axes(axs, fstr='({})', fontweight='semibold', fontsize=14)

# pg.show()
pg.savefig(str(__file__).replace('.py', '.png'), dpi=600)
