Generalised NOAH supersequences
JRJ Yong, E Kupce, TDW Claridge
===============================


Pulse programme setup
=====================

In the discussion that follows, the NOAH single-letter codes are:

 - A   : 1,1-ADEQUATE
 - Bn  : 15N HMBC
 - B   : 13C HMBC
 - S   : 13C HSQC
 - Spn : 15N seHSQC

As described in the corresponding manuscript (the PDF file in this directory),
the NOAH-4 A(Bn/B/S) experiment is designed to have a different number of scans
per module. The number of scans of the three interleaved modules (Bn, B, and S)
must add up to be the same as that for the ADEQUATE.

Section S1 contains a more detailed explanation of the pulse programme. This
README only seeks to provide the minimum required information to get started
with it.


New to NOAH?
------------

If you are entirely new to running NOAH experiments, a useful primer can be
found on the GENESIS website:

    https://nmr-genesis.co.uk

Scroll down to the FAQ and see "Acquiring NOAH experiments: an overview". This
README only describes specific points where the setup differs from that.


CNST's and NS
-------------

The first step is to choose the number of scans for each module. A sensible
setup would be something like:

 - NS(A)  = 16
 - NS(Bn) = 12
 - NS(B)  = 2
 - NS(S)  = 2

(of course, 16 = 12 + 2 + 2, so all is good). The number of scans for this
supersequence is controlled by three different CNST parameters. Specifically,
we have that:

 - NS(A)  = cnst51 * NS
 - NS(Bn) = cnst52 * NS
 - NS(B)  = cnst53 * NS

where NS is the 'overall' NS parameter seen in TopSpin. So, you could do:

 - NS = 2
 - cnst51 = 8
 - cnst52 = 6
 - cnst53 = 1

in order to get the correct number of scans for each module. Note that you do
not have to set this up for the last module, as it is automatically calculated
(in this case, NS(S) = NS(A) - NS(Bn) - NS(B)).


NBL
---

NBL should be set to 2 for all pulse programmes in this paper, because that is
the number of linearly concatenated modules. (Vertical stacking does not affect
NBL.)


TD1
---

NOAH supersequences typically require you to set TD1 to be the actual number of
t1 increments times the value of NBL. In this case, a further adjustment is
necessary, in that this must be further multiplied by cnst51. So, reusing the
example above, we have that

 - NBL    = 2
 - cnst51 = 8

If we want each module to have 256 t1 increments, then TD1 must be set to

  2 * 8 * 256 = 4096.


And the NOAH-5...?
------------------

The other pulse programme distributed here is the NOAH-5 A(Bn/B/Spn/S)
experiment. The setup here is entirely analogous to that above, except that
there are now four CNST parameters to set:

 - NS(A)   = cnst51 * NS
 - NS(Bn)  = cnst52 * NS
 - NS(B)   = cnst53 * NS
 - NS(Spn) = cnst54 * NS

Again, NS(S) is automatically calculated from the above, so you do not need to
set it. Everything else is the same as previously described.


Non-uniform sampling...
-----------------------

... doesn't work with these sequences.


Processing
==========

The NOAH-4 A(Bn/B/S) experiment should be processed using the splitx_au_13 AU
programme attached here. ('13' meaning one experiment in the first slot, and
three interleaved experiments in the second slot.)

On the other hand, the NOAH-5 A(Bn/B/S) experiment should be processed using
splitx_au_14 instead.

You can optionally set the AUNMP parameter in TopSpin to these, which allows
you to call the processing AU programme using the `xaup` command.

Note that these splitx_au_... programmes are designed to call other AU
programmes to complete processing of individual datasets. The most recent
versions of these extra AU programmes (as of the time of writing) are included
in this User Library entry, and updates are distributed via the GENESIS
website:

    https://nmr-genesis.co.uk

You should not need to set the USERP1 through USERP5 processing parameters, as
these are automatically parsed from the pulse programme during processing. For
more details of this see the GENESIS paper:

    https://doi.org/10.1021/acs.analchem.1c04964

or Jon's PhD thesis (only if you have severe, otherwise incurable, insomnia):

    https://github.com/yongrenjie/thesis


Sample data
===========

The data given here are the NOAH-4 A(Bn/B/S) spectra acquired on a sample of
brucine in CDCl3. These are the same spectra as shown in Figure 4 of the
accompanying paper.
