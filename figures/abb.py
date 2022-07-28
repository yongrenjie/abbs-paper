import penguins as pg
from aptenodytes import nmrd, fira

fira()

p = nmrd() / '220722-7c-abbs'
dss = pg.read(p, range(12001, 12004))

k = 0.8
fig, axs = pg.subplots2d(1, 3, figsize=(12*k, 4*k))

h1_bounds = (0.5, 6.3)
c13_bounds = (10, None)
n15_bounds = (110, 130)

dss[0].stage(ax=axs[0], levels=3.5e4, f1_bounds=c13_bounds, f2_bounds=h1_bounds)
dss[1].stage(ax=axs[1], levels=2.5e4, f1_bounds=n15_bounds, f2_bounds=h1_bounds)
dss[2].stage(ax=axs[2], levels=2.5e4, f1_bounds=n15_bounds, f2_bounds=h1_bounds)


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
pg.label_axes(axs, fstr='({})', fontweight='semibold', fontsize=14)

# pg.show()
pg.savefig(str(__file__).replace('.py', '.png'), dpi=600)
