import penguins as pg
import aptenodytes as apt
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import sqrtm

apt.thesis()
plt.rcParams['font.size'] = 8

fig, axs = pg.subplots2d(1, 3, figsize=(6.5, 2.3))

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
p_brucine = apt.nmrd() / '220604-7x-abbs'
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
axs[0].text(x=57, y=40, s='*', fontsize=9)
axs[0].text(x=32.5, y=40, s='*', fontsize=9)
axs[0].text(x=32.5, y=152, s='*', fontsize=9)

# (b): Cyclosporin HSQC-ADEQUATE CA-CO section, GIC, lambda=0.5
p_cyclo = apt.nmrd() / '220722-7c-abbs'
cyclo_adeq = pg.read(p_cyclo, 14001)
cyclo_c_hsqc = pg.read(p_cyclo, 14005)
stacked = np.vstack((cyclo_adeq.rr, cyclo_c_hsqc.rr))
generalised_cov = sqrtm(stacked @ stacked.T)
si1, si2 = cyclo_adeq['si'][0], cyclo_c_hsqc['si'][0]
# `cov` is a block matrix, and we only want an off-diagonal block of it.
cyclo_cov_spectrum = np.real(generalised_cov[0:si1, si1:si1+si2])
axs[1].contour(cyclo_adeq.ppm_scale(axis=0),
               cyclo_c_hsqc.ppm_scale(axis=0),
               cyclo_cov_spectrum,
               levels=generate_contour_levels(8e4),
               colors=generate_contour_colors())
axs[1].set(xlim=(43, 61), ylim=(166, 178),
           xlabel=c13_label, ylabel=c13_label)
# label peaks
axs[1].text(s='1',  x=59.2, y=169.0, fontsize=8)
axs[1].text(s='2',  x=48.9, y=174.8, fontsize=8)
axs[1].text(s='3',  x=50.7, y=171.0, fontsize=8)
axs[1].text(s='4',  x=55.7, y=168.6, fontsize=8)
axs[1].text(s='5',  x=55.2, y=175.1, fontsize=8)
axs[1].text(s='6',  x=55.2, y=172.6, fontsize=8)
axs[1].text(s='7',  x=47.4, y=171.5, fontsize=8)
axs[1].text(s='8',  x=45.1, y=173.1, fontsize=8)
axs[1].text(s='9',  x=47.0, y=170.5, fontsize=8)
axs[1].text(s='10', x=57.9, y=169.2, fontsize=8)
axs[1].text(s='11', x=58.4, y=175.0, fontsize=8)


# (c): Cyclosporin HSQC-ADEQUATE CA-CB section, GIC, lambda=0.5, symmetrised
# Symmetrisation can help with artefacts but kills responses in ADEQ from
# quaternary carbons -- not recommended
def symmetrise_preserve_sign(mat):
    # symmetrise a spectrum about main diagonal (NOTE: this is before inverting
    # the x- and y-axes so the main diagonal is mat[i,i])
    shape = mat.shape
    if shape[0] != shape[1]:
        raise ValueError("matrix must be square")
    
    smallest_amp = np.minimum(np.abs(mat), np.abs(mat).T)
    sign = np.sign(mat)
    return sign * smallest_amp
cyclo_cov_spectrum = symmetrise_preserve_sign(cyclo_cov_spectrum)
axs[2].contour(cyclo_adeq.ppm_scale(axis=0),
               cyclo_c_hsqc.ppm_scale(axis=0),
               cyclo_cov_spectrum,
               levels=generate_contour_levels(7e4),
               colors=generate_contour_colors())
axs[2].set(xlim=(6, 78), ylim=(6, 78),
           xlabel=c13_label, ylabel=c13_label)
# label peaks
axs[2].text(s='1',  x=72,   y=60,   fontsize=8)
axs[2].text(s='2',  x=53,   y=27,   fontsize=8)
axs[2].text(s='4',  x=59,   y=35.5, fontsize=8)
axs[2].text(s='5',  x=53,   y=33,   fontsize=8)
axs[2].text(s='6',  x=54,   y=40,   fontsize=8)
axs[2].text(s='7',  x=52,   y=17,   fontsize=8)
axs[2].text(s='8',  x=45,   y=16,   fontsize=8)
axs[2].text(s='9',  x=46.5, y=40,   fontsize=8)
axs[2].text(s='10', x=56,   y=45,   fontsize=8)
axs[2].text(s='11', x=60,   y=27.5, fontsize=8)

# Finishing touches
for ax in axs:
    ax.invert_xaxis()
    ax.invert_yaxis()
    pg.style_axes(ax, '2d')
    pg.ymove(ax)

pg.label_axes(axs, fstr='({})', fontweight='semibold', fontsize=8)
apt.show()
# apt.save(__file__)
