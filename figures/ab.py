import penguins as pg
from aptenodytes import nmrd, fira

fira()

p = nmrd() / '220604-7x-abbs'
dss = pg.read(p, [23001, 23002])

k = 0.8
fig, axs = pg.subplots2d(1, 2, figsize=(8*k, 4*k))

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

pg.mkplots(axs, titles=titles)
pg.ymove(axs)
pg.label_axes(axs, fstr='({})', fontweight='semibold', fontsize=14)

# pg.show()
pg.savefig(str(__file__).replace('.py', '.png'), dpi=600)
