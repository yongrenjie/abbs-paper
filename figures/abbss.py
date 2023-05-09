import penguins as pg
import aptenodytes as apt
import matplotlib.pyplot as plt

apt.thesis()
plt.rcParams['font.size'] = 12

p = apt.nmrd() / '220722-7c-abbs'
dss = pg.read(p, range(14001, 14006))

h1_bounds1 = (0.5, 6.1)
h1_bounds2 = (0.5, 8.5)
h1_bounds3 = (7.2, 8.5)
c13_bounds1 = (6, 178)
c13_bounds2 = (6, 135)
n15_bounds1 = (110, 130)
n15_bounds2 = (114, 130)

titles = [f'1,1-ADEQUATE', f'$^{{15}}$N HMBC', f'$^{{13}}$C HMBC',
          f'$^{{15}}$N seHSQC', f'$^{{13}}$C HSQC']
levels = [4.5e4, 1.8e4, 2.5e5, 2.5e5, 2.5e5]
f1bs = [c13_bounds1, n15_bounds1, c13_bounds1, n15_bounds2, c13_bounds2]
f2bs = [h1_bounds1, h1_bounds1, h1_bounds2, h1_bounds3, h1_bounds1]

for i, ds, title, level, f1b, f2b in apt.enzip(dss, titles, levels, f1bs, f2bs):
    print(f'Plotting spectrum #{i+1}...')
    fig, ax = pg.subplots2d(figsize=(3.7, 3.7))
    ds.stage(ax, levels=level, f1_bounds=f1b, f2_bounds=f2b)
    pg.mkplot(ax, title=title)
    pg.ymove(ax)
    apt.label_axes_def(ax, fontsize=12, start=i+1)
    # apt.show()
    apt.save(__file__.replace('.py', f'_{i+1}.py'))
print('Done.')
