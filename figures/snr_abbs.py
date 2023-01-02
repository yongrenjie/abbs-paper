import penguins as pg
import aptenodytes as apt
import numpy as np

p = apt.nmrd() / '221209-7x-abbs'

abbs = pg.read(p, range(12001, 12005))
bruk = pg.read(p, [31, 33, 34, 35])

titles = ['ADEQUATE', '15N HMBC', '13C HMBC', 'HSQC']
expts = [apt.Brucine.adeq, apt.Brucine.nhmbc,
         apt.Brucine.chmbc, apt.Brucine.hsqc]

for (i, title, expt,
     abbs_ds, bruk_ds) in apt.enzip(titles, expts, abbs, bruk):
    print(f'--- {title} ---')

    if i == 3:
        kw = {'edited': True}
    else:
        kw = {}

    abbs_ints = expt.integrate(abbs_ds, **kw)
    bruk_ints = expt.integrate(bruk_ds, **kw)

    rel_abbs_ints = np.mean(abbs_ints / bruk_ints)
    rel_bruk_ints = np.mean(bruk_ints / bruk_ints)

    print(f'    ABBS: {rel_abbs_ints:.4f}'
          f' -- BRUK: {rel_bruk_ints:.4f}'
          f' -- ABBS e_t: {rel_abbs_ints * np.sqrt(223/124):.4f}')
    print()
