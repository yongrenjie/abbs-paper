import penguins as pg
from aptenodytes import nmrd, fira
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm, fractional_matrix_power as powm

# Figure setup
fira()
k = 0.8
fig, axs = pg.subplots2d(1, 3, figsize=(12 * k, 4 * k))

# Contours -- basically code taken from penguins but it's not clever enough to
# do covariance spectra (maybe a future update...?)
def generate_contour_levels(base, incr=1.5, nlev=10):
    neg = [-base * (incr ** i) for i in range(nlev - 1, -1, -1)]
    pos = [base * (incr ** i) for i in range(nlev)]
    return neg + pos
def generate_contour_colors(nlev=10):
    return ["#E8000B"] * nlev + ["#023EFF"] * nlev

# Axis labels
n15_label = "$^{15}$N (ppm)"
c13_label = "$^{13}$C (ppm)"

# (a): Brucine 15N-13C correlation, UIC
p_brucine = nmrd() / '220604-7x-abbs'
brucine_n_hmbc = pg.read(p_brucine, 102002)
brucine_c_hsqc = pg.read(p_brucine, 102004)
brucine_cov_spectrum = brucine_n_hmbc.rr @ brucine_c_hsqc.rr.T
axs[0].contour(brucine_c_hsqc.ppm_scale(axis=0),
               brucine_n_hmbc.ppm_scale(axis=0),
               brucine_cov_spectrum,
               levels=generate_contour_levels(1.5e12),
               colors=generate_contour_colors())
axs[0].set(xlim=(20, 70), ylim=(25, 165),
           xlabel=c13_label, ylabel=n15_label)

# (b): Cyclosporin HSQC-ADEQUATE CA-CO section, GIC, lambda=0.5
p_cyclo = nmrd() / '220722-7c-abbs'
cyclo_adeq = pg.read(p_cyclo, 14001)
cyclo_c_hsqc = pg.read(p_cyclo, 14005)
stacked = np.vstack((cyclo_adeq.rr, cyclo_c_hsqc.rr))
generalised_cov = sqrtm(stacked @ stacked.T)
cyclo_cov_spectrum = np.real(generalised_cov[0:1024, 1024:2048])
axs[1].contour(cyclo_adeq.ppm_scale(axis=0),
               cyclo_c_hsqc.ppm_scale(axis=0),
               cyclo_cov_spectrum,
               levels=generate_contour_levels(8e4),
               colors=generate_contour_colors())
axs[1].set(xlim=(43, 61), ylim=(166, 178),
           xlabel=c13_label, ylabel=c13_label)

# (c): Cyclosporin HSQC-ADEQUATE CA-CB section, GIC, lambda=0.5
axs[2].contour(cyclo_adeq.ppm_scale(axis=0),
               cyclo_c_hsqc.ppm_scale(axis=0),
               cyclo_cov_spectrum,
               levels=generate_contour_levels(1e5),
               colors=generate_contour_colors())
axs[2].set(xlim=(6, 78), ylim=(6, 78),
           xlabel=c13_label, ylabel=c13_label)

# Finishing touches
for ax in axs:
    ax.invert_xaxis()
    ax.invert_yaxis()
    pg.style_axes(ax, '2d')
    pg.ymove(ax)
pg.label_axes(axs, fstr='({})', fontweight='semibold', fontsize=14)
# pg.show()
pg.savefig(str(__file__).replace('.py', '.png'), dpi=600)
