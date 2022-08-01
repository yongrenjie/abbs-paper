import penguins as pg
import aptenodytes as apt
import numpy as np

p = apt.nmrd() / '220604-7x-abbs'

abbs = pg.read(p, range(102001, 102005))
bruk = pg.read(p, range(31, 35))
noah = pg.read(p, range(41, 45))

titles = ['ADEQUATE', '15N HMBC', '13C HMBC', 'HSQC']
expts = [apt.Brucine.adeq, apt.Brucine.nhmbc,
         apt.Brucine.chmbc, apt.Brucine.hsqc]

for (i, title, expt,
     abbs_ds, bruk_ds, noah_ds) in apt.enzip(titles, expts,
                                             abbs, bruk, noah):
    print(f'--- {title} ---')

    if i == 3:
        kw = {'edited': True}
    else:
        kw = {}

    abbs_ints = expt.integrate(abbs_ds, **kw)
    bruk_ints = expt.integrate(bruk_ds, **kw)
    noah_ints = expt.integrate(noah_ds, **kw)

    rel_abbs_ints = np.mean(abbs_ints / bruk_ints)
    rel_bruk_ints = np.mean(bruk_ints / bruk_ints)
    rel_noah_ints = np.mean(noah_ints / bruk_ints)

    print(f'    ABBS: {rel_abbs_ints:.4f}'
          f' -- BRUK: {rel_bruk_ints:.4f}'
          f' -- NOAH: {rel_noah_ints:.4f}')
    if i == 1:
        # abbs_ds.f2projp().stage(label='abbs')
        # bruk_ds.f2projp().stage(label='bruk')
        # noah_ds.f2projp().stage(label='noah')
        # pg.mkplot(); pg.show()
        print('    note: ABBS was acquired with longer 15N gradients')
    print()
