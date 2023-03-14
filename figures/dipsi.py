import penguins as pg
import aptenodytes as apt
import matplotlib.pyplot as plt
import numpy as np

apt.thesis()
plt.rcParams['font.size'] = 8

p = apt.nmrd() / '220604-7x-abbs'
hsqc_with_dipsi = pg.read(p, 13004)
hsqc_without_dipsi = pg.read(p, 22004)

dipsi_ints = apt.Brucine.hsqc.integrate(hsqc_with_dipsi, edited=True)
no_dipsi_ints = apt.Brucine.hsqc.integrate(hsqc_without_dipsi, edited=True)
print(np.mean(dipsi_ints/no_dipsi_ints))


fig, axs = pg.subplots2d(1, 3, figsize=(6.4, 2.4))

baselev = 1e6
hbounds = (1.1, 8)
cbounds = (23, 131)
hsqc_with_dipsi.stage(axs[0], levels=baselev, f1_bounds=cbounds, f2_bounds=hbounds)
hsqc_without_dipsi.stage(axs[1], levels=baselev, f1_bounds=cbounds, f2_bounds=hbounds)
pg.mkplot(axs[0], title="With 35 ms DIPSI")
pg.mkplot(axs[1], title="Without DIPSI")
pg.ymove(axs[0])
pg.ymove(axs[1])


# fancy legend handler code stolen from penguins which was in turn stolen from
# stack overflow
 
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerBase  # type: ignore
class ContourLegendHandler(HandlerBase):
    # code lifted mostly from https://stackoverflow.com/a/41765095/
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        line_cpos = plt.Line2D([x0, y0 + width], [0.7 * height, 0.7 * height],
                               color=orig_handle[0])
        line_cneg = plt.Line2D([x0, y0 + width], [0.3 * height, 0.3 * height],
                               color=orig_handle[1])
        return [line_cpos, line_cneg]

hbounds2 = (1.1, 5)
hsqc_with_dipsi.f2projp().stage(axs[2], bounds=hbounds2,
                                color=pg.color_palette("pastel")[0])
hsqc_with_dipsi.f2projn().stage(axs[2], bounds=hbounds2,
                                color=pg.color_palette("pastel")[3])
hsqc_without_dipsi.f2projp().stage(axs[2], bounds=hbounds2,
                                   color=pg.color_palette("deep")[0])
hsqc_without_dipsi.f2projn().stage(axs[2], bounds=hbounds2,
                                   color=pg.color_palette("deep")[3])
pg.mkplot(axs[2], title="$F_2$ projections")
legend_colors = [(pg.color_palette('pastel')[0], pg.color_palette('pastel')[3]),
                 (pg.color_palette('deep')[0], pg.color_palette('deep')[3])]
legend_labels = ['DIPSI', 'no DIPSI']
axs[2].legend(legend_colors, legend_labels, fontsize=8, loc='upper center',
              handler_map={tuple: ContourLegendHandler()})

apt.label_axes_def(axs, fontsize=8)
# apt.show()
apt.save(__file__)
